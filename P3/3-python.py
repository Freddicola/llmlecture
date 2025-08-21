import dotenv
dotenv.load_dotenv()

"""python 프로그램을 실행시키는 도구"""

from langchain_experimental.tools import PythonREPLTool
tool = PythonREPLTool()

# 활용: LLM으로 python 코드를 생성하고 실행할 수 있다.
# 예시: LLM이 python 코드를 생성하고, 이를 실행하여 결과를 반환

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
output_parser = StrOutputParser()

# chain = prompt | llm | output_parser | tool
from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("다음을 만족하는 python code를 생성하라: {objective}")

from langchain.chat_models import init_chat_model
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

chain = prompt | llm | output_parser | tool
result = chain.invoke({"objective": """
- 100과 200을 더하는 python 코드를 작성하라. 
- 실제 동작하는 코드만 출력하라. 
- 마크다운은 사용하지 말 것. 
- 즉 ```python 표시는 사용하지 말 것."""})
print(result)  # Output: "print(100 + 200)"

