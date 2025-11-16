from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph

from .nodes.classifier import node_classifier
from .nodes.products import products_node
from .nodes.general import general_node

def build_graph() -> CompiledStateGraph:
    graph = StateGraph()

    graph.add_node(START, "start")
    graph.add_node("classifier", node_classifier)
    graph.add_node("products", products_node)
    graph.add_node("general", general_node)
    graph.add_node(END, "end")

    graph.add_edge(START, "classifier")
    graph.add_edge("classifier", "products", condition=lambda state: state["intent"] == "products")
    graph.add_edge("classifier", "general", condition=lambda state: state["intent"] == "general")
    graph.add_edge("products", END)
    graph.add_edge("general", END)

    return graph.compile()

graph = build_graph()
