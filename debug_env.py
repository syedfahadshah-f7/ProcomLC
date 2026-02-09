
import os
import sys
from src.utils.config import Config

def mask_key(key):
    if not key:
        return "Not Set"
    if len(key) < 8:
        return "****"
    return f"{key[:4]}...{key[-4:]}"

def main():
    print("="*60)
    print("DEBUG: Checking Environment Variables")
    print("="*60)
    
    # Force reload of config/env
    Config.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    Config.DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY", "")
    
    print(f"Current Working Directory: {os.getcwd()}")
    print("-" * 60)
    print(f"OPENAI_API_KEY Status:   {mask_key(Config.OPENAI_API_KEY)}")
    print(f"DEEPGRAM_API_KEY Status: {mask_key(Config.DEEPGRAM_API_KEY)}")
    print("-" * 60)
    
    if not Config.OPENAI_API_KEY:
        print("❌ ERROR: OPENAI_API_KEY is missing!")
        print("Please check your .env file in the project root.")
    else:
        print("✅ OPENAI_API_KEY found.")

    if not Config.DEEPGRAM_API_KEY:
        print("⚠️  WARNING: DEEPGRAM_API_KEY is missing (Stage 1 diarization will be skipped)")
    else:
        print("✅ DEEPGRAM_API_KEY found.")
        
    print("="*60)

if __name__ == "__main__":
    main()
