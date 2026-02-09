"""Configuration management for LangChain Mysteries competition."""

import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Config:
    """Configuration class for managing API keys and settings."""
    
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "")
    DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY", "")
    
    # Model Configuration
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
    
    # Paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    DATA_DIR = os.path.join(BASE_DIR, "data")
    DUMMY_AUDIO_DIR = os.path.join(DATA_DIR, "dummy_audio")
    DUMMY_DOCUMENTS_DIR = os.path.join(DATA_DIR, "dummy_documents")
    DUMMY_CASE_DIR = os.path.join(DATA_DIR, "dummy_case")
    
    # Competition Settings
    STAGE1_AUDIO_COUNT = 4
    STAGE2_QUESTIONS_COUNT = 6
    STAGE3_QUESTIONS_COUNT = 6
    
    @classmethod
    def validate(cls):
        """Validate that required API keys are set."""
        if not cls.OPENAI_API_KEY:
            print("WARNING: OPENAI_API_KEY not set. LLM features will not work.")
            return False
        return True
    
    @classmethod
    def get_openai_api_key(cls):
        """Get OpenAI API key with fallback to dummy mode."""
        if cls.OPENAI_API_KEY:
            return cls.OPENAI_API_KEY
        print("Using dummy mode - no API key provided")
        return "dummy_key_for_testing"


# Create directories if they don't exist
for directory in [Config.DATA_DIR, Config.DUMMY_AUDIO_DIR, 
                  Config.DUMMY_DOCUMENTS_DIR, Config.DUMMY_CASE_DIR]:
    os.makedirs(directory, exist_ok=True)
