from langchain_openai import ChatOpenAI

from app.schemas.agent_state import AgentState

def node_classifier(state: AgentState) -> AgentState:
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
    content = response.content.strip()

    state["intent"] = content
    return state