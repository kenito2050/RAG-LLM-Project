import os
import pytest
import requests
from langchain_openai import ChatOpenAI
from ragas import SingleTurnSample
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import LLMContextPrecisionWithoutReference
from utils import get_llm_response, load_test_data

#user_input -> query
#response -> response
#reference -> Ground truth
#retrived_context -> Top k retrieved docs

@pytest.mark.asyncio
@pytest.mark.parametrize("getData",
                         load_test_data("Context_Precision_test_data.json"),
                         indirect=True
                         )
async def test_context_precision(llm_wrapper, getData):
    # create object of class for that specific metric
    #power of LLM + method metric ->score
    context_precision = LLMContextPrecisionWithoutReference(llm=llm_wrapper)
    #score
    score = await context_precision.single_turn_ascore(getData)
    print(score)
    assert score > 0.8

    # question = "How many articles are there in the Selenium webdriver python course?"
    # # Feed data -
    # responseDict = requests.post("https://rahulshettyacademy.com/rag-llm/ask",
    #                              json={
    #                                  "question": question,
    #                                  "chat_history": [
    #                                  ]
    #                              }).json()
    # print(responseDict)

@pytest.fixture
def getData(request):
    test_data = request.param
    responseDict = get_llm_response(test_data)
    sample = SingleTurnSample(
        user_input=test_data["question"],
        retrieved_contexts=[doc["page_content"] for doc in responseDict.get("retrieved_docs")],
        response="23"
    )
    return sample


    # sample = SingleTurnSample(
    #     user_input=question,
    #     response=responseDict["answer"],
    #     retrieved_contexts=[doc["page_content"] for doc in responseDict.get("retrieved_docs")]
    # )