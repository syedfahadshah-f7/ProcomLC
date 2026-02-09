try:
    from langchain_classic.chains.combine_documents import create_stuff_documents_chain
    print("create_stuff_documents_chain imported successfully")
except ImportError as e:
    print(f"ImportError: {e}")
except Exception as e:
    print(f"Error: {e}")
