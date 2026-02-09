try:
    from langchain_core.prompts import PromptTemplate
    print("PromptTemplate imported from langchain_core.prompts")
    print(f"Type: {type(PromptTemplate)}")
except ImportError as e:
    print(f"ImportError: {e}")
