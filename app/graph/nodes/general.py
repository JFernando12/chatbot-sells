from langchain_openai import ChatOpenAI

from app.schemas.agent_state import AgentState

def general_node(state: AgentState) -> AgentState:
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)
    query = state["query"]
    
    prompt = f"""
    Responde a la siguiente consulta del usuario de manera clara y concisa:
    Consulta: "{query}"
    """
    
    response = llm.invoke(prompt)
    content = response.content.strip()
    
    state["response"] = content
    return state