import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
try:
    from stage1_audio.stage1_audio_pipeline import AudioIntelligencePipeline
    print("AudioIntelligencePipeline imported successfully")
    pipeline = AudioIntelligencePipeline()
    from langchain_core.prompts import PromptTemplate
    print(f"PromptTemplate: {PromptTemplate}")
    from langchain_classic.chains import LLMChain
    print(f"LLMChain: {LLMChain}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
