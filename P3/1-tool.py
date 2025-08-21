from langchain_core.tools import tool

@tool(parse_docstring=True)
def add(a: int, b: int) -> int:
    """Add two numbers.
    
    Args:
        a (int): the left operand.
        b (int): the right operand.
    
    Returns:
        The sum of the two operands.
    """
    return a + b

print(type(add))
print(add.name)
print(add.description)
print(add.args)

response = add.invoke({"a": 2, "b": 3})
print(response)

"""
LLM이 tool을 사용할 수 있게 한다.
"""

from langchain_core.runnables import RunnableLambda

inc = RunnableLambda(lambda x: x + 1)
inc = inc.as_tool(name="increment", description="Increment a number by 1")

print(type(inc))
print(inc.name)
print(inc.description)
print(inc.args)
