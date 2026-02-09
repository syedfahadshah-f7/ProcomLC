"""
Audio Generator for Stage 1 Testing
Creates dummy audio files with embedded clues for the mystery case.
"""

import os
from gtts import gTTS
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.config import Config


class AudioGenerator:
    """Generate dummy audio files for testing Stage 1."""
    
    def __init__(self, output_dir: str = None):
        """Initialize audio generator."""
        self.output_dir = output_dir or Config.DUMMY_AUDIO_DIR
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_audio(self, text: str, filename: str, save_transcript: bool = True):
        """
        Generate audio file from text using gTTS.
        
        Args:
            text: Text to convert to speech
            filename: Output filename (without extension)
            save_transcript: Whether to save the transcript as well
        """
        audio_path = os.path.join(self.output_dir, f"{filename}.mp3")
        transcript_path = os.path.join(self.output_dir, f"{filename}_transcript.txt")
        
        # Generate audio using gTTS
        try:
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(audio_path)
            print(f"✓ Generated audio: {audio_path}")
        except Exception as e:
            print(f"✗ Error generating audio for {filename}: {e}")
            print("  Continuing with transcript only...")
        
        # Save transcript
        if save_transcript:
            with open(transcript_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"✓ Saved transcript: {transcript_path}")
    
    def generate_mystery_case_audio(self, scenario: str = "A"):
        """
        Generate audio files for the specified scenario.
        
        Args:
            scenario: 'A' for original case, 'B' for new test case
        """
        if scenario == "A":
            self._generate_scenario_a()
        elif scenario == "B":
            self._generate_scenario_b()
        else:
            print(f"Unknown scenario: {scenario}")

    def _generate_scenario_a(self):
        """Generate Original Case: The Poisoned Researcher."""
        
        # Audio 1: Security Interview
        audio1_text = """
        Security Guard Interview - Officer Martinez (CASE A)
        Date: January 15th, 2026, 9:30 AM
        
        My name is Officer Carlos Martinez. I've been working the night shift at the research facility
        for about three years now. On the night of January 14th, between 11 PM and midnight, I noticed
        something unusual. Dr. Sarah Chen accessed the building using her keycard at 11:47 PM, which was
        strange because she usually leaves by 6 PM.
        
        I saw her walking towards the biochemistry lab on the third floor. She was carrying a large bag
        and seemed nervous. About twenty minutes later, I heard what sounded like glass breaking from
        that area. When I went to investigate, Dr. Chen was leaving the building in a hurry. She said
        she forgot some important documents and had to retrieve them urgently.
        
        The next morning, we discovered that Dr. Robert Kane was found unconscious in the lab. That's all
        I know about the incident.
        """
        
        # Audio 2: Lab Assistant Statement
        audio2_text = """
        Lab Assistant Statement - Michael Torres (CASE A)
        Date: January 15th, 2026, 2:00 PM
        
        I'm Michael Torres, lab assistant in the biochemistry department. I work closely with both
        Dr. Robert Kane and Dr. Sarah Chen. On January 14th, I was in the lab until about 8 PM working
        on some experiments.
        
        I remember Dr. Kane was acting strangely that day. He was very protective of a new compound he
        had been developing. He mentioned something about having evidence that someone was stealing
        research data and selling it to competitors. He said he was going to expose them soon.
        
        There was tension between Dr. Kane and Dr. Chen recently. They had a heated argument last week
        about research priorities and budget allocation. Dr. Kane accused someone of accessing the
        financial records without authorization. I also noticed that Professor James Mitchell had been
        spending unusually long hours in the lab lately, often arriving late at night.
        """
        
        # Audio 3: Witness Account
        audio3_text = """
        Witness Account - Professor Emily Watson (CASE A)
        Date: January 16th, 2026, 10:00 AM
        
        Professor Emily Watson here from the chemistry department. I was working late on January 14th
        in my office on the fourth floor. Around 10:30 PM, I went down to the cafeteria for coffee.
        
        On my way back, I saw Professor James Mitchell entering the biochemistry lab. He seemed startled
        when he saw me and quickly explained that he needed to check on some shared equipment. What struck
        me as odd was that he was wearing gloves and carrying what looked like cleaning supplies.
        
        I also saw the system administrator, David Park, in the building that evening around 9 PM. He was
        accessing the server room. I know this because I needed IT help earlier that week, and David
        mentioned he would be performing system maintenance on the 14th. The server logs would show who
        accessed which files that night.
        """
        
        # Audio 4: Emergency Call Recording
        audio4_text = """
        Emergency Call Recording - 911 Dispatch (CASE A)
        Date: January 15th, 2026, 7:15 AM
        
        911 what's your emergency?
        
        Caller: This is Dr. Lisa Park calling from the University Research Facility on Campus Drive.
        We've found Dr. Robert Kane unconscious in the biochemistry lab. He's not responding. We need
        an ambulance immediately.
        
        Dispatcher: Is he breathing?
        
        Caller: Yes, but his pulse is weak. There's a strange chemical smell in the lab, and we found
        broken glassware on the floor. It looks like there might have been a struggle or an accident.
        Some of the lab notebooks are scattered around, and the secure cabinet where we store experimental
        compounds is open. Dr. Kane was known to be working on a breakthrough formula. Several files
        are missing from his desk.
        
        Dispatcher: Help is on the way. Please evacuate the area immediately due to potential chemical
        exposure.
        
        Caller: Understood. We're evacuating now.
        """
        
        # Generate all audio files
        print("\nGenerating Stage 1 Audio Files (Scenario A)...")
        print("="*80 + "\n")
        
        self.generate_audio(audio1_text, "audio1_security_interview")
        self.generate_audio(audio2_text, "audio2_lab_assistant")
        self.generate_audio(audio3_text, "audio3_witness_account")
        self.generate_audio(audio4_text, "audio4_emergency_call")
        
        print("\n✓ All Scenario A audio files generated successfully!")

    def _generate_scenario_b(self):
        """Generate New Test Case: The Sabotaged Prototype."""
        
        # Audio 1: CEO Statement - Case B
        audio1_text = """
        CEO Interview - Marcus Thorne (CASE B)
        Date: March 10th, 2026, 8:00 AM
        
        I arrived at the Robotics Lab at 7 AM to check on the 'Apex' prototype before the investor demo.
        I found the prototype completely destroyed. The main CPU was smashed, and the servo motors were
        ripped out.
        
        Only three people had access codes to the lab last night: Lead Engineer Elena Rostova, 
        Intern Kevin Miller, and our competitor's former employee who we just hired, Victor Krum.
        
        I know Elena was furious about the project timeline. She said it was 'impossible' to finish.
        But destroying her own work? I don't know.
        """

        # Audio 2: Intern Statement - Case B
        audio2_text = """
        Intern Statement - Kevin Miller (CASE B)
        Date: March 10th, 2026, 9:15 AM
        
        I left the lab at 8 PM. Everything was fine. The Apex robot was standing in the center of the room.
        I did see Victor Krum lingering around the server room door. He looked... suspicious. He was 
        on his phone, speaking in a hushed tone. I heard him say 'It will be done tonight'.
        
        Elena left before me, around 7:30 PM. She seemed stressed but not angry. She actually high-fived
        me on her way out, saying the calibration was finally perfect.
        """

        # Audio 3: Janitor Witness - Case B
        audio3_text = """
        Janitor Witness - Old Man Jenkins (CASE B)
        Date: March 10th, 2026, 10:45 AM
        
        I was mopping the hallway outside the secure lab. Around 9:30 PM, I saw someone enter the lab.
        They used a keycard. I couldn't see their face clearly, but they were wearing a red hoodie.
        
        I know for a fact that Victor Krum owns a red hoodie. I've seen him wear it to work.
        About 15 minutes later, I heard loud crashing noises. Bang! Smash! I thought maybe the robot fell over.
        The person ran out a minute later.
        """

        # Audio 4: Security Log Voice Memo - Case B
        audio4_text = """
        Security System Voice Log (CASE B)
        Date: March 9th, 2026, 9:31 PM
        
        Access Granted: User Victor Krum.
        Location: Secure Robotics Lab.
        Method: Keycard + Pin.
        
        ... [Silence for 15 minutes] ...
        
        Audio Sensor Triggered: High Decibel Impact Detected.
        Glass Break Sensor: Triggered.
        
        9:46 PM: Exit Detected. User: Victor Krum.
        Door Left Ajar Alarm.
        """

        print("\nGenerating Stage 1 Audio Files (Scenario B)...")
        print("="*80 + "\n")
        
        self.generate_audio(audio1_text, "audio1_ceo_interview")
        self.generate_audio(audio2_text, "audio2_intern_statement")
        self.generate_audio(audio3_text, "audio3_janitor_witness")
        self.generate_audio(audio4_text, "audio4_security_log")
        
        print("\n✓ All Scenario B audio files generated successfully!")

        print(f"Location: {self.output_dir}")


def main():
    """Main function to generate dummy audio files."""
    generator = AudioGenerator()
    generator.generate_mystery_case_audio()


if __name__ == "__main__":
    main()
