import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

from langchain_core.vectorstores import InMemoryVectorStore
vector_store = InMemoryVectorStore(embeddings)

docs = [
    "사과는 빨간색도 있고, 초록색도 있습니다. 나는 빨간 사과는 좋아하지만 초록 사과는 싫어합니다.",
    "바나나는 노란색입니다. 바나나는 맛있습니다. 나는 바나나를 좋아합니다.",
    "포도는 보라색입니다. 포도는 작고 달콤합니다. 포도는 씨가 있어서 먹기 불편합니다. 나는 포도를 싫어합니다.",
    "나는 낚시를 좋아합니다. 낚시는 물고기를 잡는 재미가 있습니다. 낚시는 자연과 함께하는 활동입니다.",
    "나는 여행을 좋아합니다. 여행을 통해 다양한 과일을 맛볼 수 있습니다.",
]
query = "내가 좋아하는 과일은?"

vector_store.add_texts(docs)

response = vector_store.similarity_search(query, k=3)  # k는 검색할 문서의 개수
print(f"가장 유사한 문서들: {response}")

