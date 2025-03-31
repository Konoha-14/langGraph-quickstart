from config import _set_env
from chatbot import build_state_graph
from IPython.display import Image, display
import os

if __name__ == "__main__":
    # _set_env("ANTHROPIC_API_KEY")
    # print(os.environ.get("ANTHROPIC_API_KEY"))
    graph = build_state_graph()
    try:
        display(Image(graph.get_graph().draw_mermaid_png()))
    except Exception:
        # This requires some extra dependencies and is optional
        print("An exception occured while displaying the graph")