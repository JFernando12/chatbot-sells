from typing_extensions import TypedDict

class AgentState(TypedDict):
    user_id: str
    query: str
    intent: str
    response: str