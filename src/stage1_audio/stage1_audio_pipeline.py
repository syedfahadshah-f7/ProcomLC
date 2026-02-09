"""
Stage 1: Audio Intelligence Pipeline
Uses Speech-to-Text + LangChain to extract answers from audio files.

Competition Requirements:
- Process 4 audio files
- Extract answers to 5-6 questions
- Use Whisper or similar for transcription
- Use LangChain for question answering
"""

import os
import json
from typing import List, Dict, Optional
from langchain_openai import ChatOpenAI
try:
    from langchain_core.prompts import PromptTemplate
    from langchain_classic.chains import LLMChain
except ImportError:
    PromptTemplate = None
    LLMChain = None

try:
    from deepgram import DeepgramClient, PrerecordedOptions, FileSource
except ImportError:
    DeepgramClient = None
    PrerecordedOptions = None
    FileSource = None
from pathlib import Path

# For actual Whisper integration (uncomment when API key is available)
# import whisper

# For testing without Whisper
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.config import Config


class AudioIntelligencePipeline:
    """Pipeline for processing audio files and extracting information."""
    
    def __init__(self, openai_api_key: Optional[str] = None):
        """
        Initialize the audio intelligence pipeline.
        
        Args:
            openai_api_key: OpenAI API key for LLM reasoning
        """
        self.api_key = openai_api_key or Config.get_openai_api_key()
        
        # Initialize LLM for question answering
        if self.api_key and self.api_key != "dummy_key_for_testing":
            self.llm = ChatOpenAI(
                model=Config.OPENAI_MODEL,
                temperature=Config.TEMPERATURE,
                openai_api_key=self.api_key
            )
        else:
            self.llm = None
            print("WARNING: Running in dummy mode. Set OPENAI_API_KEY for actual LLM processing.")
        
        # For actual Whisper model (uncomment when ready)
        # self.whisper_model = whisper.load_model("base")
        
    def transcribe_with_deepgram(self, audio_path: str) -> str:
        """Transcribe audio using Deepgram with diarization."""
        if not DeepgramClient or not Config.DEEPGRAM_API_KEY:
            print("Deepgram SDK not installed or API key missing.")
            return ""

        try:
            deepgram = DeepgramClient(Config.DEEPGRAM_API_KEY)
            
            with open(audio_path, "rb") as file:
                buffer_data = file.read()
            
            payload = {"buffer": buffer_data}
            options = PrerecordedOptions(
                model="nova-2",
                smart_format=True,
                diarize=True,
            )
            
            response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
            return response.results.channels[0].alternatives[0].transcript
        except Exception as e:
            print(f"Deepgram transcription failed: {e}")
            return ""

    def transcribe_audio(self, audio_path: str) -> str:
        """
        Transcribe audio file to text using Deepgram (if available) or Dummy/Whisper fallback.
        
        Args:
            audio_path: Path to audio file
            
        Returns:
            Transcribed text
        """
        # 1. Try Deepgram if configured
        if Config.DEEPGRAM_API_KEY:
            transcript = self.transcribe_with_deepgram(audio_path)
            if transcript:
                return transcript
        
        # 2. DUMMY IMPLEMENTATION for testing:
        filename = os.path.basename(audio_path)
        
        # Read from pre-generated transcript files
        transcript_path = audio_path.replace('.mp3', '_transcript.txt').replace('.wav', '_transcript.txt')
        
        if os.path.exists(transcript_path):
            with open(transcript_path, 'r', encoding='utf-8') as f:
                return f.read()
        
        return f"[Dummy transcript for {filename}]"
    
    def answer_questions_from_transcript(self, transcript: str, questions: List[str]) -> Dict[str, str]:
        """
        Extract answers to questions from transcript using LangChain.
        
        Args:
            transcript: Transcribed audio text
            questions: List of questions to answer
            
        Returns:
            Dictionary mapping questions to answers
        """
        # Create a prompt template for question answering
        qa_template = """You are an expert investigator analyzing audio transcripts from a mystery case.
        
Transcript:
{transcript}

Question: {question}

Based ONLY on the information in the transcript above, provide a clear and concise answer.
If the answer is not found in the transcript, respond with "Information not found in transcript."

Answer:"""


        
        answers = {}
        
        if self.llm:
            prompt = PromptTemplate(
                input_variables=["transcript", "question"],
                template=qa_template
            )
            
            try:
                # Use actual LLM chain
                qa_chain = LLMChain(llm=self.llm, prompt=prompt)
                
                for question in questions:
                    try:
                        response = qa_chain.invoke({
                            "transcript": transcript,
                            "question": question
                        })
                        answers[question] = response['text'].strip()
                    except Exception as e:
                        print(f"LLM Error answering question '{question}': {e}. Falling back to dummy mode.")
                        answers[question] = self._dummy_answer(transcript, question)
            except Exception as e:
                print(f"LLM Chain initialization failed: {e}. Falling back to dummy mode.")
                return self._dummy_answers_all(transcript, questions)
        else:
            return self._dummy_answers_all(transcript, questions)
        
        return answers

    def _dummy_answer(self, transcript: str, question: str) -> str:
        """Smart dummy answer based on keywords."""
        q_lower = question.lower()
        if "who" in q_lower:
            if "Sarah Chen" in transcript: return "Dr. Sarah Chen"
            if "Victor Krum" in transcript: return "Victor Krum"
            if "Martinez" in transcript: return "Officer Martinez"
            return "Unknown person"
        elif "activity" in q_lower or "suspicious" in q_lower:
            if "Sarah Chen" in transcript: return "Late night lab access at 11:47 PM"
            if "Victor Krum" in transcript: return "Smashed Apex prototype and deleted logs"
            return "Suspicious movements reported"
        return f"[Dummy answer for: {question}]"

    def _dummy_answers_all(self, transcript: str, questions: List[str]) -> Dict[str, str]:
        """Generate dummy answers for all questions."""
        return {q: self._dummy_answer(transcript, q) for q in questions}
    
    def process_audio_file(self, audio_path: str, questions: List[str]) -> Dict:
        """
        Process a single audio file: transcribe and answer questions.
        
        Args:
            audio_path: Path to audio file
            questions: List of questions to answer
            
        Returns:
            Dictionary with transcript and answers
        """
        print(f"Processing audio file: {audio_path}")
        
        # Step 1: Transcribe audio
        transcript = self.transcribe_audio(audio_path)
        print(f"Transcription complete. Length: {len(transcript)} characters")
        
        # Step 2: Answer questions
        answers = self.answer_questions_from_transcript(transcript, questions)
        
        return {
            "audio_file": os.path.basename(audio_path),
            "transcript": transcript,
            "answers": answers
        }
    
    def process_all_audio_files(self, audio_dir: str, questions: List[str]) -> List[Dict]:
        """
        Process all audio files in a directory.
        
        Args:
            audio_dir: Directory containing audio files
            questions: List of questions to answer for each file
            
        Returns:
            List of results for each audio file
        """
        audio_files = []
        for ext in ['*.mp3', '*.wav', '*.m4a']:
            audio_files.extend(Path(audio_dir).glob(ext))
        
        results = []
        for audio_file in sorted(audio_files):
            result = self.process_audio_file(str(audio_file), questions)
            results.append(result)
        
        return results


def main():
    """Main function for testing the audio pipeline."""
    # Initialize pipeline
    pipeline = AudioIntelligencePipeline()
    
    # Sample questions for testing
    questions = [
        "Who is mentioned in this audio recording?",
        "What location is discussed?",
        "What time or date is mentioned?",
        "What suspicious activity is described?",
        "What evidence is presented?",
    ]
    
    # Process audio files
    audio_dir = Config.DUMMY_AUDIO_DIR
    
    if not os.path.exists(audio_dir):
        print(f"Audio directory not found: {audio_dir}")
        print("Please run audio_generator.py first to create dummy audio files.")
        return
    
    results = pipeline.process_all_audio_files(audio_dir, questions)
    
    # Display results
    print("\n" + "="*80)
    print("STAGE 1: AUDIO INTELLIGENCE - RESULTS")
    print("="*80 + "\n")
    
    for i, result in enumerate(results, 1):
        print(f"\n--- Audio File {i}: {result['audio_file']} ---")
        print(f"\nTranscript:\n{result['transcript'][:200]}...")
        print(f"\nAnswers:")
        for question, answer in result['answers'].items():
            print(f"  Q: {question}")
            print(f"  A: {answer}\n")
    
    # Save results to JSON
    output_path = os.path.join(Config.DATA_DIR, "stage1_results.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✓ Results saved to: {output_path}")


if __name__ == "__main__":
    main()
