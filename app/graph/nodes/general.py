from langchain_openai import ChatOpenAI

from ..state.state import AgentState

def general_node(state: AgentState) -> dict:
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)
    query = state["query"]
    
    prompt = f"""
    Responde a la siguiente consulta del usuario de manera clara y concisa:
    Consulta: "{query}"
    """
    
    response = llm.invoke(prompt)
    return {"response": response.strip()}