import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# pip install wikipedia
from langchain_community.retrievers import WikipediaRetriever
retriever = WikipediaRetriever()

from langchain.schema.runnable import RunnablePassthrough

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("""다음 context를 근거로 질문에 답하세요.
context: {context}
question: {question}
""")

chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm

response = chain.invoke("한국의 대통령은?")

print(response)