import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from google import genai

client = genai.Client()
image = client.files.upload(file="./data/일출.jpg")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[image, "사진에 대해 설명해줘"]
)

print(response.text)

"""
사진들을 이렇게 문서화 할 수 있다면, 사진 검색에 매우 유용할 것이다.
"""