import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

# pip install ragas rapidfuzz
# 설명: Ragas는 LangChain과 통합되어, LLM을 사용하여 데이터셋에 대한 테스트 세트를 생성하는 도구입니다.
from ragas.testset import TestsetGenerator
generator = TestsetGenerator.from_langchain(llm, embeddings)

docs = [Document(page_content=text) for text in []

# Load the documents from the CSV file
dataset = generator.generate_with_langchain_docs(docs, testset_size=10)
df = dataset.to_pandas()
df.to_csv('dataset.csv', index=False)
