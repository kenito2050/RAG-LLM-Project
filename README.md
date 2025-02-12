# RAG-LLM-Project
 RAG-LLM_Evaluation_Project
 
This project demonstrates the RAGAS Pytest Framework for evaluating \ testing AI-based RAG-LLM applications.
This project was written in Python and uses the RAGAS Pytest Framework.
Original source for this project comes from the following online Udemy Course: https://www.udemy.com/course/rag-llm-evaluation-ai-test/

To Use:

1 - Download project files
2 - To run scripts, You will need to purchase an API KEY from OPEN AI.
	See https://www.geeksforgeeks.org/how-to-get-your-own-openai-api-key/
3 - Search for the following text and replace [Key] with the your purchased API KEY.
	os.environ["OPENAI_API_KEY"] = "[Key]"
4 - To upload results for test_Response_Relevancy_Factual_Correctness_Results_Upload.py to https://app.ragas.io/dashboard, you will need to create a RAGAS APP TOKEN. 
	See https://docs.ragas.io/en/stable/getstarted/rag_eval/
5 - After creating a RAGAS APP TOKEN, search for the following text and replace [TOKEN] with the your RAGAS APP TOKEN.
	os.environ["RAGAS_APP_TOKEN"] = "[Token]"

6 - The following scripts perform the corresponding AI Evaluation Tests:

Context Recall - 2 Scripts

test_Context_Recall_no_Framework.py
test_Context_Recall_with_Framework

Context Precision - 2 Scripts

test_Context_Precision_no_Framework.py
test_Context_Precision_with_Framework.py

Faithfulness - 1 Script

test_Faithfulness_with_Framework.py

Response Relevancy & Factual Correctness - 1 Script

test_Response_Relevancy_Factual_Correctness_Results_Upload.py

Topic Adherence - 1 Script

test_Topic_Adherence_with_Framework.py

Rubric Score - 1 Script

test_Rubric_Score.py

7 - Here is a brief summary (including definitions, formulas & examples) for calculating each AI Evaluation metric

###Context Recall###

Definition: Measures the proportion of relevant documents that are successfully retrieved out of all the relevant documents available in the dataset. 

Formula:

Recall = Number of relevant documents retrieved / Total number of relevant documents

Example: 

Query: "Causes of deforestation." 

Ground truth (relevant documents): 5 documents. 

Retrieved documents: 3 

Recall = 3/5 = 0.6 (60%). 

###Context Precision###
 
Definition: Measures the proportion of retrieved documents that are relevant to the query out of all the documents retrieved. 

Formula:

Precision = Number of relevant documents retrieved / Total number of documents retrieved

Query: "Causes of deforestation." 

Retrieved documents: 5 total, of which 3 are relevant and 2 are irrelevant. 

Precision = 3/5​=0.6 (60%).

How Context Recall & Context Precision complement each other
High Recall + Low Precision: Many relevant documents are retrieved, but there’s also a lot of noise (irrelevant documents). 
High Precision + Low Recall: Most retrieved documents are relevant, but some important ones are missing. 
High Recall + High Precision: Ideal case—comprehensive and accurate retrieval. 

In practice: 
Recall is prioritized when missing relevant documents is costly (e.g., medical research, legal discovery). 
Precision is prioritized when irrelevant information can overwhelm the user (e.g., search engine queries). 

###Faithfulness###

Faithfulness metric measures the factual consistency of the generated answer against the given context. 
It is calculated from answer and retrieved context. The answer is scaled to (0.1) range. Higher the better. 1    
Faithfulness score = (Number of claims in the generated answer that can be inferred from given context) / (Total number of claims in the generated answer) 

User input: 
How many articles and downloadable resources are there in the Selenium WebDriver python course? 

Retrieved contexts: Complete Understanding on Selenium Python API Methods with real time Scenarios on LIVE Websites\n"Last but not least" you can clear any Interview and can Lead Entire Selenium Python Projects from Design Stage\nThis course includes:\n17.5 hours on-demand video\nAssignments\n23 articles\n9 downloadable resources\nAccess on mobile and TV\nCertificate of completion\nRequirements 

High faithfulness answer: There are 23 articles and 9 downloadable resources. 
Low faithfulness answer: There are 23 articles and downloadable resources varies from course

###Response Relevancy ###
metric focuses on assessing how pertinent the generated answer is to the given prompt. A lower score is assigned to answers that are incomplete or contain redundant information and higher scores indicate better relevancy.  
Assessment of answer relevance does not consider factuality but instead penalizes cases where the answer lacks completeness or contains redundant details. To calculate this score, the LLM is prompted to generate an appropriate question for the generated answer multiple times, and the mean cosine similarity between these generated questions and the original question is measured. 

Example: 
Question: Where is France and what is it's capital? 
Low relevance answer: France is in western Europe. 
High relevance answer: France is in western Europe and Paris is its capital.

Difference between Faithfulness & Response Relevancy
Faithfulness metric measures the number of factual claims of the generated answer against the given retrieval context where as Response Relevancy metric focuses on assessing how relevant the generated answer is to the given prompt

###Factual Correctness###
Factual Correctness is a metric that compares and evaluates the factual accuracy of the generated response with the reference (ground truth/expected value). This metric is used to determine the extent to which the generated response aligns with the reference. The factual correctness score ranges from 0 to 1, with higher values indicating better performance. 

###Rubrics based criteria scoring###
This metric that is used to evaluate response. The rubric consists of descriptions for each score, typically ranging from 1 to 10. The response here is evaluation based on score_descriptions and ground truth. 

rubrics = { 
    "score1_description": "The response is incorrect, irrelevant, or does not align with the ground truth.", 
    "score2_description": "The response partially matches the ground truth but includes significant errors, omissions, or irrelevant information.", 
    "score3_description": "The response generally aligns with the ground truth but may lack detail, clarity, or have minor inaccuracies.", 
    "score4_description": "The response is mostly accurate and aligns well with the ground truth, with only minor issues or missing details.", 
    "score5_description": "The response is fully accurate, aligns completely with the ground truth, and is clear and detailed.", 
} 

user_input="Where is the Eiffel Tower located?", 
response="The Eiffel Tower is located in Europe and it is part of France.", 
reference="The Eiffel Tower is located in Paris.", 
