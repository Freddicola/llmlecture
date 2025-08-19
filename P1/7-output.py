import dotenv
dotenv.load_dotenv()

from pydantic import BaseModel, Field


class CountryCapital(BaseModel):
    country: str = Field(description="국가 이름")   # description: LLM이 이해할 수 있는 필드 설명
    capital: str = Field(description="국가의 수도")


from langchain_core.output_parsers import JsonOutputParser
output_parser = JsonOutputParser(pydantic_object=CountryCapital)

print(output_parser.get_format_instructions())

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("{country}의 수도는? 출력은 다음 형식으로. {format}")

from langchain.chat_models import init_chat_model
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
chain = prompt | llm | output_parser

response = chain.invoke({"country": "중국", "format": output_parser.get_format_instructions()})
print(response)


