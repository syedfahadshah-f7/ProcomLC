try:
    print("Trying imports...")
    from langchain_openai import ChatOpenAI
    print("ChatOpenAI imported")
    from langchain_core.prompts import PromptTemplate
    print("PromptTemplate imported")
    from langchain.chains import LLMChain
    print("LLMChain imported")
    from langchain.chains.combine_documents import create_stuff_documents_chain
    print("create_stuff_documents_chain imported")
    from langchain_core.documents import Document
    print("Document imported")
except ImportError as e:
    print(f"ImportError: {e}")
except Exception as e:
    print(f"Error: {e}")
