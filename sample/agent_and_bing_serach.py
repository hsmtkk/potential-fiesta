from langchain_openai import OpenAI
from langchain.agents.load_tools import load_tools
from langchain.agents.agent import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain import hub


# https://future-coders.net/langchain%E5%85%A5%E9%96%80-6agent-%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88/

llm = OpenAI()
tools = load_tools(["bing-search"])
prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
agent_exe = AgentExecutor(
    agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
)
agent_exe.invoke(
    {"input": "昨日の東京の最高気温は何度か? 昨日の気温はインターネットから検索せよ。"}
)
