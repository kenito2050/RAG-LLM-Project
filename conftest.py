import os
import pytest
from langchain_openai import ChatOpenAI
from ragas.llms import LangchainLLMWrapper

os.environ["OPENAI_API_KEY"] = "[Key]"
os.environ["RAGAS_APP_TOKEN"] = "[Token]"

@pytest.fixture
def llm_wrapper():
    llm = ChatOpenAI(model="gpt-4o",temperature=0)
    lang_chain_llm = LangchainLLMWrapper(llm)
    return lang_chain_llm