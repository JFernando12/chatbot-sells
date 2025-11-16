from ..state.state import AgentState
from langchain_openai import ChatOpenAI

def node_classifier(state: AgentState) -> dict:
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)
    query = state["query"]
    prompt = f"""
    Clasifica la siguiente consulta del usuario en una de las siguientes categorias:
    1. products: Informacion de productos
    2. buy_intent: Intento de compra
    3. general: Informacion general
    Consulta: "{query}"
    Responde solo con la categoria correspondiente.
    """
    response = llm.invoke(prompt)
    return {"intent": response.strip()}