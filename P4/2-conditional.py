from typing import TypedDict
from langgraph.types import Command

class CounterState(TypedDict):
    counter: int


class UserInputState(TypedDict):
    user_input: str


def get_user_input(state: CounterState) -> Command:
    print(f"Counter value: {state['counter']}")
    user_input = input("Input (+, -, .): ")
    
    if user_input == "+":
        return Command(goto="increment")
    elif user_input == "-":
        return Command(goto="decrement")
    elif user_input == ".":
        return Command(goto=END)
    
    print("Invalid input. Please enter +, -, or .")
    return Command(goto="get_user_input")


from langgraph.graph import StateGraph, START, END
graph = StateGraph(CounterState)

graph.add_node("get_user_input", get_user_input)
graph.add_edge(START, "get_user_input")

def increment(state: CounterState) -> Command:
    return Command(update={"counter": state["counter"] + 1}, goto="get_user_input")

def decrement(state: CounterState) -> Command:
    return Command(update={"counter": state["counter"] - 1}, goto="get_user_input")

def check_func(state: UserInputState):
    return state["user_input"]

graph.add_node("increment", increment)
graph.add_node("decrement", decrement)

graph.add_conditional_edges(
    "get_user_input",
    check_func,
    {
        "+": "increment",  # if + then go to increment
        "-": "decrement",  # if - then go to decrement
        ".": END,  # if . then finish
    })

graph.add_edge("increment", "get_user_input")
graph.add_edge("decrement", "get_user_input")

app = graph.compile()
response = app.invoke({"counter": 0})

print(response)

