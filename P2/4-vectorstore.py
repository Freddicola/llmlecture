import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.vectorstores import PostgresVectorStore
vector_store = InMemoryVectorStore(embeddings)

"""vector_store를 사용하는 DB도 존재한다. 대표적인 예로는 ChromaDB가 있다.
PostgresVectorStore는 벡터 데이터를 저장할 테이블을 필요로 합니다. 일반적으로 라이브러리가 자동으로 테이블을 생성하지만, 필요 시 직접 생성할 수도 있습니다.
"""

texts = [
    "2025년 6월 3일에 당선된 제 21대 대통령은 더불어민주당 이재명이다.",
    "한국의 수도는 서울이다. 서울은 대한민국의 수도이자 최대 도시이다.",
]

vector_store.add_texts(texts)

response = vector_store.similarity_search("한국의 대통령은?", k=1) # k는 검색할 문서의 개수
print(response[0].page_content)  # Output: "2025년 6월 3일에 당선된 제 21대 대통령은 더불어민주당 이재명이다."

