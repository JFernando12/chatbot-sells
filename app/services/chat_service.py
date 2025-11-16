from app.graph.graph import graph
from app.schemas.agent_state import AgentState

class ChatService:
  def send(self, message: str) -> str:
      initial_state: AgentState = {
          "user_id": "anonymous",
          "query": message,
          "intent": "",
          "response": ""
      }
      result = graph.invoke(initial_state)
      response = result['response']
      return response
  
chat_service = ChatService()