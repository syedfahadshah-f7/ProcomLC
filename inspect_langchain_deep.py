import langchain
print(f"File: {langchain.__file__}")
print(f"Path: {langchain.__path__}")
try:
    import langchain.chains
    print("langchain.chains imported")
except ImportError as e:
    print(f"ImportError chains: {e}")

try:
    from langchain.chains import LLMChain
    print("LLMChain imported")
except ImportError as e:
    print(f"ImportError LLMChain: {e}")

import langchain_community
print(f"Community File: {langchain_community.__file__}")
