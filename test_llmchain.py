try:
    from langchain.chains import LLMChain
    print("LLMChain imported from langchain.chains")
except ImportError as e:
    print(f"ImportError from langchain.chains: {e}")

try:
    from langchain_classic.chains import LLMChain
    print("LLMChain imported from langchain_classic.chains")
except ImportError as e:
    print(f"ImportError from langchain_classic.chains: {e}")
