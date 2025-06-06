from langchain_openai import ChatOpenAI

from langgraph.graph import StateGraph, END

from langchain.agents import AgentExecutor, create_openai_tools_agent

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.tools import tool

from datetime import datetime, timezone
from typing import TypedDict


from dotenv import load_dotenv

load_dotenv()

# Инструмент времени
@tool
def get_current_time() -> dict:
    """Return the current UTC time in ISO‑8601 format."""
    return {"utc": datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}

# Состояние
class ChatState(TypedDict):
    message: str

# Модель
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Шаблон
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful assistant."),
    MessagesPlaceholder(variable_name="messages"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# Агент
agent = create_openai_tools_agent(llm, [get_current_time], prompt)
agent_executor = AgentExecutor(agent=agent, tools=[get_current_time])

# Обработка
def run_agent(state: ChatState) -> ChatState:
    user_message = HumanMessage(content=state["message"])

    result = agent_executor.invoke({"messages": [user_message]})
    agent_answer = result['output']

    return {"message": agent_answer}

# Граф
workflow = StateGraph(ChatState)
workflow.add_node("agent", run_agent)
workflow.set_entry_point("agent")
workflow.add_edge("agent", END)
app = workflow.compile()
