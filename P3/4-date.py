import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_core.tools import tool
from datetime import datetime


"""
tool의 description을 기록하는 것은 LLM에서 사용될 수 있도록, 정보를 주는 과정
"""
@tool
def get_current_time() -> str:
    """오늘 날짜를 제공합니다.
    
    Arguments:
    - None
    """
    return datetime.now().strftime("%Y년 %m월 %d일 %A")

from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    ("system", "오늘 날짜와 요일은 'get_current_time' 도구를 사용하여 알 수 있습니다."),
    ("human", "{question}"),
    MessagesPlaceholder("agent_scratchpad")
])

agent = create_tool_calling_agent(
    llm=llm,
    tools=[get_current_time],
    prompt=prompt)

agent_executor = AgentExecutor(agent=agent, tools=[get_current_time])

response = agent_executor.invoke({"question": "모레는 몇일인가요?"})
print(response)