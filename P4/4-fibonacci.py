import operator
from typing import TypedDict, Annotated, Literal

class FibonacciState(TypedDict):
    N: int
    fibonacci: Annotated[list[int], operator.add]
    result: int


from langgraph.graph import StateGraph, START, END
graph = StateGraph(FibonacciState)

graph.add_node("fibonacci", lambda _: {"fibonacci": [0, 1]})
graph.add_node("calculate_fibonacci", lambda state: {
    "fibonacci": state["fibonacci"][-1] + state["fibonacci"][-2]
    })
graph.add_node("exit_fibonacci", lambda state: {
    "result": state["fibonacci"][state["N"]]
    })

graph.add_edge(START, "fibonacci")
graph.add_conditional_edges(
    "fibonacci",
    lambda state: "exit" if len(state["fibonacci"]) > state["N"] else "next",
    {
        "next": "calculate_fibonacci",
        "exit": "exit_fibonacci"
    })

graph.add_conditional_edges(
    "calculate_fibonacci",
    lambda state: "exit" if len(state["fibonacci"]) > state["N"] else "next",  # 다음 state 결정
    {
        "next": "calculate_fibonacci",
        "exit": "exit_fibonacci"
    })

graph.add_edge("exit_fibonacci", END)
app = graph.compile()
response = app.invoke({"N": 5})

print(response)

