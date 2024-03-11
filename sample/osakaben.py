from langchain_openai import ChatOpenAI
from langchain_core.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains.sequential import SimpleSequentialChain

llm = ChatOpenAI(temperature=0.5)

prompt1 = PromptTemplate(
    input_variables=["english"],
    template="Please translate this text to Japanese: {english}",
)
chain1 = LLMChain(llm=llm, prompt=prompt1)

prompt2 = PromptTemplate(
    input_variables=["japanese"], template="以下の文章を大阪弁に変換せよ: {japanese}"
)
chain2 = LLMChain(llm=llm, prompt=prompt2)

seq = SimpleSequentialChain(chains=[chain1, chain2], verbose=True)

resp = seq.invoke(
    "OpenAI offers a spectrum of models with different levels of power suitable for different tasks."
)

print(resp)
