from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(temperature=0.5)

messages = [HumanMessage(content="Who are you?")]

resp = chat.invoke(messages)

print(resp)
