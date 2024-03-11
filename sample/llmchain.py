from langchain_openai import ChatOpenAI
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.chains import LLMChain

llm = ChatOpenAI(temperature=0.5)

system_template = (
    "You are a helpful chatbot that translate {input_language} to {output_language}"
)
system_prompt = SystemMessagePromptTemplate.from_template(system_template)
human_template = "{text}"
human_prompt = HumanMessagePromptTemplate.from_template(human_template)
prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])

llm_chain = LLMChain(prompt=prompt, llm=llm)
text = "OpenAI offers a spectrum of models with different levels of power suitable for different tasks."

resp = llm_chain.invoke(
    {"input_language": "English", "output_language": "Japanese", "text": text}
)

print(resp)
