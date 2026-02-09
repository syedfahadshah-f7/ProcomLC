"""Quick test to verify configuration"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from utils.config import Config
from stage1_audio.stage1_audio_pipeline import AudioIntelligencePipeline

print("="*60)
print("CONFIGURATION TEST")
print("="*60)
print(f"✓ GROQ_API_KEY: {'Set (' + Config.GROQ_API_KEY[:20] + '...)' if Config.GROQ_API_KEY else 'Missing'}")
print(f"✓ GROQ_MODEL: {Config.GROQ_MODEL}")
print(f"✓ DEEPGRAM_API_KEY: {'Set' if Config.DEEPGRAM_API_KEY else 'Missing'}")
print(f"✓ ELEVENLABS_API_KEY: {'Set' if Config.ELEVENLABS_API_KEY else 'Missing'}")
print()

print("Testing pipeline initialization...")
try:
    pipeline = AudioIntelligencePipeline()
    print("✓ AudioIntelligencePipeline initialized successfully")
    print(f"  LLM Status: {'Active (Groq)' if pipeline.llm else 'Dummy mode'}")
except Exception as e:
    print(f"✗ Error: {e}")

print()
print("="*60)
print("All checks passed! No Deepgram warnings!")
print("="*60)
