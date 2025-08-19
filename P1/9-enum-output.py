import dotenv
dotenv.load_dotenv()

from enum import Enum
class Color(Enum):
    RED    = "빨강"
    BLUE   = "파랑"
    YELLOW = "노랑"

from langchain.output_parsers import EnumOutputParser
output_parser = EnumOutputParser(enum=Color)

"""
# EnumOutputParser는 Enum 클래스의 멤버를 출력 형식으로 사용합니다.
# 예를 들어, Color.RED, Color.BLUE, Color.YELLOW 중 하나로 대답해야 합니다.
"""
print(output_parser.get_format_instructions())

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("{flower}의 색깔은? 출력은 다음 형식으로. {format}")

print(prompt)

from langchain.chat_models import init_chat_model
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
chain = prompt | llm | output_parser

# response = chain.invoke({"flower": "해바라기", "format": output_parser.get_format_instructions()})
response = chain.invoke({"flower": "해바라기", "format": "빨강, 파랑, 노랑 중 하나로 대답하세요."})
print(response)  