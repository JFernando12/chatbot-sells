from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph

from app.schemas.agent_state import AgentState
from .nodes.classifier import node_classifier
from .nodes.products import products_node
from .nodes.general import general_node

def build_graph() -> CompiledStateGraph:
    graph = StateGraph(state_schema=AgentState)

    graph.add_node("classifier", node_classifier)
    graph.add_node("products", products_node)
    graph.add_node("general", general_node)

    graph.add_edge(START, "classifier")
    graph.add_edge("products", END)
    graph.add_edge("general", END)

    graph.add_conditional_edges(
        "classifier",
        lambda s: s.get("intent"),
        {
            "products": "products",
            "general": "general",
        }
    )

    return graph.compile()

graph = build_graph()
