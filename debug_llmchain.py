try:
    from langchain_classic.chains import LLMChain
    print("LLMChain imported successfully")
except Exception as e:
    print(f"Error importing LLMChain: {e}")
    import traceback
    traceback.print_exc()
