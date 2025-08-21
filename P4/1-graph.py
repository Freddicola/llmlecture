from typing import TypedDict
class CounterState(TypedDict):
    counter: int

from langgraph.graph import StateGraph, START, END
graph = StateGraph(CounterState)


# 함수는 node이다.
def increment(state: CounterState) -> CounterState:
    state["counter"] += 1
    return state

print(increment.__name__)
graph.add_node("increment", increment)

# graph.set_entry_point("increment")
graph.add_edge(START, "increment")

# graph.set_finish_point("increment")
graph.add_edge("increment", END)

app = graph.compile()
response = app.invoke({"counter": 0})
print(response)

with open("1-graph.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())
