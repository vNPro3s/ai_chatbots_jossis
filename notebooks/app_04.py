import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

env_path = os.path.join(os.getcwd(), '.env')
# loading the environment variables
load_dotenv(dotenv_path=env_path)

print(os.getenv('OPENAI_API_KEY'))
# define the model
llm = "gpt-4o"

# Simple Sequential Chain

# input -> | LLM -> output -> input -> LLM  |-> output

model = ChatOpenAI(model=llm, api_key=os.getenv('OPENAI_API_KEY'))

title_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
    You are an experienced journalist. Provide only one catching title for an article about {topic}.""")


essay_prompt = PromptTemplate(
    input_variables=["title"],
    template="""
    As an expert nonfiction writer, write an essay about {title} not longer \
    than 250 words but do not include length in a title.
    Make sure that an essay is enganging and informative. \
    Include at least one short quote from a famous person.""")


fst_chain = title_prompt | model | StrOutputParser()
snd_chain = essay_prompt | model 
chain = fst_chain | snd_chain

st.title("LangChain Chatbot")

topic = st.text_input("Enter a topic.")

if topic:
    response = chain.invoke({"topic": topic})
    st.write(response.content)