import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("""
다음 내용을 참고하여 질문에 답하라
{context}
질문: {question}""")


chain = prompt | llm

response = chain.invoke({"context": """
제21대 대통령 선거 개표 결과 이재명 더불어민주당 후보가 대통령에 당선됐다.
중앙선거관리위원회에 따르면 4일 오전 5시 10분 개표율 100%를 기준으로 이재명 후보가 49.42%를 득표하며 당선을 확정 지었다. 앞서 3일 밤 12시 기준 개표 작업이 약 50% 정도 진행된 상황에서 이 후보의 당선이 확실시됐다. 중앙선관위는 4일 오전 6시 전체위원회의를 개최해 이재명 후보를 대통령 당선인으로 공식 확정했다.
한편 이번 21대 대선의 최종 투표율은 79.4%로 잠정 집계됐다. 지난 20대 대선보다 2.3%포인트 높으며, 28년만 최고 투표율이다.""",
"question": "한국의 대통령은?"})

"""기사의 내용이 context 이다.
교재 95쪽"""
print(response.content)
