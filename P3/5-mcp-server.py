# pip install langchain-mcp-adapters
from mcp.server.fastmcp import FastMCP

# Math라는 이름의 MCP 서버를 생성합니다.
mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    mcp.run(transport="streamable-http")  # HTTP를 통해 8000번 포트에서 서버를 실행합니다.
