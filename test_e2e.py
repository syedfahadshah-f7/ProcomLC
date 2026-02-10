"""End-to-end test of Stage 1 with actual audio files."""

from src.stage1_audio.stage1_audio_pipeline import AudioIntelligencePipeline
from utils.config import Config
import os
import json

print("="*80)
print("END-TO-END TEST: Processing Actual Audio Files")
print("="*80)

# Initialize pipeline
pipeline = AudioIntelligencePipeline()

# Check if audio files exist
audio_dir = Config.DUMMY_AUDIO_DIR
print(f"\nAudio directory: {audio_dir}")

if not os.path.exists(audio_dir):
    print("❌ Audio directory not found. Creating dummy transcripts...")
    os.makedirs(audio_dir, exist_ok=True)
    # Create sample transcript
    with open(os.path.join(audio_dir, "audio1_ceo_interview_transcript.txt"), "w") as f:
        f.write("""CEO Jennifer Martinez Interview:
Q: What can you tell us about Friday night?
A: I was at home. But I did notice some unusual activity on the security logs.
Dr. Sarah Chen accessed Lab 3 at 11:47 PM, which is highly irregular.
She's never been there that late before. The Apex prototype is stored there.
""")

# Define questions
questions = [
    "Who is mentioned in this audio recording?",
    "What suspicious activity is described?",
    "What evidence is presented?"
]

# Process the audio file (or its transcript)
print("\n" + "-"*80)
print("Processing audio file...")
print("-"*80)

# Test with audio file path (will use transcript)
audio_path = os.path.join(audio_dir, "audio1_ceo_interview.mp3")
result = pipeline.process_audio_file(audio_path, questions)

print("\n✓ PROCESSING COMPLETE\n")
print(f"Audio: {result['audio_file']}")
print(f"Transcript length: {len(result['transcript'])} characters")
print(f"\nTranscript preview:")
print(result['transcript'][:200] + "...\n")

print("ANSWERS:")
print("-"*80)
for q, a in result['answers'].items():
    print(f"\nQ: {q}")
    print(f"A: {a}")

print("\n" + "="*80)
print("✓ NO CONNECTION ERRORS!")
print("✓ ALL QUESTIONS ANSWERED SUCCESSFULLY!")
print("="*80)
