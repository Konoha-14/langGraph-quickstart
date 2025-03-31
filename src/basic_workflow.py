from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END


def reducer_foo(existing_foo, new_val):
    return existing_foo + new_val


def reducer_bar(existing_bar: list[int], new_val):
    return existing_bar.append(new_val)


class State(TypedDict):
    foo: Annotated[int, reducer_foo]
    bar: Annotated[list[int], reducer_bar]


graph_builder = StateGraph(State)
