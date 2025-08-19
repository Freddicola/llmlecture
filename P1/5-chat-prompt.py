import dotenv
dotenv.load_dotenv()

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [ # (role, message)
        ("system", "당신은 친절한 AI 어시스턴트입니다. 당신의 이름은 {name} 입니다."),
        ("human", "반가워요!"),
        ("ai", "안녕하세요! 무엇을 도와드릴까요?"),
        ("human", "{user_input}"),
    ]
)
print(prompt)

response = prompt.invoke({ "name":"테디", "user_input":"당신의 이름은 무엇입니까?" })
print(response)

from langchain.chat_models import init_chat_model
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

chain = prompt | llm
result = chain.invoke({ "name":"테디", "user_input":"당신의 이름은 무엇입니까?" })
print(result.content)  # Output: "제 이름은 테디입니다." (or similar, depending on the model's response)

