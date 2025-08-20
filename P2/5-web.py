import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_community.document_loaders import WebBaseLoader


import bs4

# 웹에서 기사를 로드합니다. URL은 예시로 사용되며, 실제 URL로 변경해야 합니다.
# BeautifulSoup를 사용하여 HTML을 파싱하고, 기사를 로드합니다.
# 이 과정에서 필요한 경우 BeautifulSoup의 파서 옵션을 조정할 수 있습니다.
loader = WebBaseLoader("https://news.naver.com/article/001/0015568637", 
                       bs_kwargs=dict(parse_only=bs4.SoupStrainer("article")))

docs = loader.load()
print(docs)

response = llm.invoke("다음 기사를 요약해줘 " + docs[0].page_content)

print(response.content)  # Output: 요약된 기사 내용