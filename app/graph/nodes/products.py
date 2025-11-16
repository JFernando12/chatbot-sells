from langchain_openai import ChatOpenAI

from app.schemas.agent_state import AgentState

products = [
  {
    "id": "prod_001",
    "name": "Wireless Mouse",
    "description": "A high-precision wireless mouse with ergonomic design.",
    "price": 29.99,
  },
  {
    "id": "prod_002",
    "name": "Mechanical Keyboard",
    "description": "A durable mechanical keyboard with customizable RGB lighting.",
    "price": 79.99,
  },
  {
    "id": "prod_003",
    "name": "HD Monitor",
    "description": "A 24-inch HD monitor with vibrant colors and sharp images.",
    "price": 149.99,
  },
]

def products_node(state: AgentState) -> AgentState:
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)
    query = state["query"]
    
    product_list = "\n".join([f"{p['name']}: {p['description']} (Price: ${p['price']})" for p in products])
    
    prompt = f"""
    Basandote en la siguiente lista de productos, responde a la consulta del usuario de manera clara y concisa.
    
    Lista de productos:
    {product_list}
    
    Consulta del usuario: "{query}"
    """
    
    response = llm.invoke(prompt)
    content = response.content.strip()
    
    state["response"] = content
    return state