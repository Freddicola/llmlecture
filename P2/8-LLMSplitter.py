import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("""다음 문장을 내용별로 나눠주는데, 각 단위는 ***로 구분해줘: {content}""")

chain = prompt | llm

with open("AI 에이전트 동향.txt", "r", encoding="utf-8") as f:
    file = f.read()
    # print(file)

    response = chain.invoke({"content": file})

    print(response.content)  # Output: 나눠진 내용
    print("=" * 20)
    docs = response.content.split("***")
    print(f"document count: {len(docs)}")
    print(docs)  # Output: 나눠진 내용


from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

from langchain_core.vectorstores import InMemoryVectorStore
vector_store = InMemoryVectorStore(embeddings)

vector_store.add_texts(docs)

from langchain_core.runnables import RunnablePassthrough

retriever = vector_store.as_retriever()

prompt = PromptTemplate.from_template("""다음 context를 근거로 질문에 답하세요.
context: {context}
question: {question}
""")


# LLM에 retriever를 통해서 지식을 전달한다.
# retriever는 context를 가져오는 역할을 한다.
chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm

response = chain.invoke("AI 에이전트 동향은?")

print("=" * 20)
print(response.content)  # Output: AI 에이전트 동향에 대한 답변
