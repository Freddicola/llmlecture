from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

from langchain_chroma import Chroma
vector_store = Chroma(embedding_function=embeddings, persist_directory="chroma_db")

searched = vector_store.similarity_search(
               "흡연과 주차가 가능하고 맛에 대한 평가가 80점 이상인 레스토랑을 추천해줘.", k=3)
for item in searched:
    print(item)
