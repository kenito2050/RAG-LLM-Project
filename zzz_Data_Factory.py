import os
from langchain_community.document_loaders import DirectoryLoader, UnstructuredWordDocumentLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.llms import LangchainLLMWrapper
from ragas.testset import TestsetGenerator
import nltk

os.environ["OPENAI_API_KEY"] = "[Key]"
os.environ["RAGAS_APP_TOKEN"] = "[Token]"

nltk.data.path.append("C:/Python_Projects/LLM_Evaluation/nltk_data")
llm = ChatOpenAI(model="gpt-4",temperature=0)
langchain_llm = LangchainLLMWrapper(llm)
embed = OpenAIEmbeddings()
loader = DirectoryLoader(
    path= "C:/Python_Projects/LLM_Evaluation/fs11",
    glob="**/*.docx",
    loader_cls= UnstructuredWordDocumentLoader
)
docs = loader.load()
generate_embeddings = LangchainEmbeddingsWrapper(embed)
generator = TestsetGenerator(llm=langchain_llm, embedding_model=generate_embeddings)
dataset = generator.generate_with_langchain_docs(docs, testset_size=20)
print(dataset.to_list())
dataset.upload()