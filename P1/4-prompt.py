import dotenv
dotenv.load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

prompt = PromptTemplate.from_template("{country}의 수도는?")
print(prompt)

result = prompt.invoke({"country": "한국"})
print(result)  # Output: "한국의 수도는?" (or similar, depending on the model's response)

from langchain_core.runnables import RunnableSequence

chain = RunnableSequence(prompt, llm)
result = chain.invoke({"country": "한국"})
print(result.content)  # Output: "한국의 수도는 서울입니다." (or similar