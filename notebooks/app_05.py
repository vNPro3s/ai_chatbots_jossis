import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
import streamlit as st

env_path = os.path.join(os.getcwd(), '.env')
# loading the environment variables
load_dotenv(dotenv_path=env_path)

print(os.getenv('OPENAI_API_KEY'))
# define the model
llm = "gpt-4o"

model = ChatOpenAI(model=llm, api_key=os.getenv('OPENAI_API_KEY'))


title_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
    You are an experienced journalist. Provide only one catching title for an article about {topic}.""")

essay_prompt = PromptTemplate(  
    input_variables=["title", "emotion"],
    template="""
    As an expert nonfiction writer, write an essay about {title} not longer than 250 words but do not include length in a title.
    Make sure that an essay is enganging and informative, and makes reader to feel {emotion}. Include at least one short quote from a 
    famous person.
    Format the output as a JSON object with the following keys 'title', 'emotion' and 'essay' with corresponding values.""")

fst_chain = title_prompt | model | StrOutputParser()
snd_chain = essay_prompt | model | JsonOutputParser()

chain = (fst_chain |(lambda title: {"title": title, "emotion": emotion})| snd_chain)

st.title("LangChain Chatbot")

topic = st.text_input("Enter a topic.")
emotion = st.text_input("Enter an emotion.")

if topic and emotion:
    response = chain.invoke({"topic": topic})
    # write the title from the response
    st.write(response)
    st.write(response["title"])
    st.write(response["emotion"])
    st.write(response["essay"])