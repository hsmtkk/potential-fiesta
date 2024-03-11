from langchain_openai import ChatOpenAI
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

system_template = (
    "You are a helpful chatbot that translate {input_language} to {output_language}"
)
system_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template = "{text}"
human_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat = ChatOpenAI(temperature=0.5)
chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])

resp = chat.invoke(
    chat_prompt.format_prompt(
        input_language="English",
        output_language="Japanese",
        text="This notebook covers how to get started with OpenAI chat models.",
    )
)

print(resp)
