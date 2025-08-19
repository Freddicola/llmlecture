import dotenv
dotenv.load_dotenv()

from langchain.output_parsers import DatetimeOutputParser
output_parser = DatetimeOutputParser()

print(output_parser.get_format_instructions())

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("{company}의 창립일은? 출력은 다음 형식으로. {format}")

from langchain.chat_models import init_chat_model
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
chain = prompt | llm | output_parser

response = chain.invoke({"company": "삼성", "format": output_parser.get_format_instructions()})
print(response.strftime("%Y-%m-%d"))  # Output: "1938-03-22" (or similar, depending on the model's response)

