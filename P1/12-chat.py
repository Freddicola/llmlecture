import dotenv
dotenv.load_dotenv()

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 나의 친구입니다. 편안하게 대화해 주세요."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{user_input}")
])

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
chain = prompt | llm

history = []
while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("대화를 종료합니다.")
        break

    response = chain.invoke({"history": history, "user_input": user_input})
    print(f"AI: {response.content}")

    history.append({"role": "human", "content": user_input})
    history.append({"role": "ai", "content": response.content})
    
"""
(.venv) C:\ProjectGit\llmabok>C:/ProjectGit/llmabok/.venv/Scripts/python.exe c:/ProjectGit/llmabok/P1/12-chat.py
You: 내 이름은 김정식이야
AI: 정식 씨, 안녕하세요! 만나서 반가워요. 저는 당신의 친구가 될 수 있어서 기쁩니다. 오늘 하루는 어떠셨나요? 편하게 이야기해주세요. 😊
You: 내가 뭐라고 했지?
AI: 방금 "내 이름은 김정식이야" 라고 말씀하셨어요. 😊 뭘 도와드릴까요?
You: exit
대화를 종료합니다.
"""
