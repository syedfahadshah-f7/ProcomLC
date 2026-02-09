from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

try:
    llm = ChatOpenAI(openai_api_key=api_key)
    response = llm.invoke("Hello, are you there?")
    print(f"Response: {response.content}")
except Exception as e:
    print(f"Error: {e}")
