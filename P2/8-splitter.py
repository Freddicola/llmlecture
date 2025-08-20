with open("AI 에이전트 동향.txt", "r", encoding="utf-8") as f:
    file = f.read()

from langchain_text_splitters import CharacterTextSplitter
splitter = CharacterTextSplitter(separator="\n")

docs = splitter.create_documents([file])

with open("AI 에이전트 동향_Splitted.txt", "w", encoding="utf-8") as f:
    f.write(f"Number of splitted documents: {len(docs)}")
    for doc in docs:
        f.write(f"\n\n---\n\n{doc.page_content}")


from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter()

docs = splitter.create_documents([file])

with open("AI 에이전트 동향_RSplitted.txt", "w", encoding="utf-8") as f:
    f.write(f"Number of splitted documents: {len(docs)}")
    for doc in docs:
        f.write(f"\n\n---\n\n{doc.page_content}")

# from langchain_experimental.text_splitter import SemanticChunker
# from langchain_huggingface import HuggingFaceEmbeddings
# embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

# splitter = SemanticChunker(embeddings=embeddings)

# docs = splitter.create_documents([file])

# with open("AI 에이전트 동향_SSplitted.txt", "w", encoding="utf-8") as f:
#     f.write(f"Number of splitted documents: {len(docs)}")
#     for doc in docs:
#         f.write(f"\n\n---\n\n{doc.page_content}")
