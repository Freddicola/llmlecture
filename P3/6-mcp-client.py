import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

# Initialize MCP client with a math server using stdio transport
client = MultiServerMCPClient(
    {
        # "math": {
        #     "command": "python",
        #     "args": ["P3/5-mcp-server.py"],
        #     "transport": "stdio",
        # }
        "math": {
            "url": "http://localhost:8000/mcp",  # Example URL for a running MCP server
            "transport": "streamable_http",  # Use HTTP transport for the MCP server
        }
    }
)


import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


async def main():
    tools = await client.get_tools()  # asynchronous call to get tools
    print(tools)

    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Math MCP 서버를 사용하여 수학 연산을 수행합니다."),
        ("human", "{question}"),
        MessagesPlaceholder("agent_scratchpad")
    ])

    from langchain.agents import create_tool_calling_agent, AgentExecutor
    agent = create_tool_calling_agent(llm, tools, prompt)
    executor = AgentExecutor(agent=agent, tools=tools)

    response = await executor.ainvoke({"question": "2와 3을 더하면 얼마인가요?"})
    print(response)


asyncio.run(main())  # run the main function asynchronously

