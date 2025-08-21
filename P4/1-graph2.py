from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class InputState(TypedDict):
    input: str


class OutputState(TypedDict):
    output: str


class PrivateState(TypedDict):
    private: str


class OverallState(TypedDict):
    input: InputState
    output: OutputState
    private: PrivateState


graph = StateGraph(OverallState)


def node_1(state: InputState) -> PrivateState:
    state["input"] = "Hello, World!"
    return {"private": state["input"] + " is private"}


def node_2(state: PrivateState) -> OutputState:
    return {"output": state["private"] + " and this is output"}

graph.add_node("node_1", node_1)
graph.add_node("node_2", node_2)

graph.add_edge(START, "node_1")
graph.add_edge("node_1", "node_2")
graph.add_edge("node_2", END)

app = graph.compile()

response = app.invoke({"input": "Initial input"})
print(response)

