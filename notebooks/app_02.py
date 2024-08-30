import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import streamlit as st

env_path = os.path.join(os.getcwd(), '.env')
# loading the environment variables
load_dotenv(dotenv_path=env_path)

print(os.getenv('OPENAI_API_KEY'))
# define the model
llm = "gpt-4o"


model = ChatOpenAI(model=llm, api_key=os.getenv('OPENAI_API_KEY'))

prompt = PromptTemplate(
    input_variables=["country", "model_name"],
    template="""What are the top 5 cities in {country}? \
    Answer with a ordered list of cities and its population size.\
    On the end provide model: {model_name}"""
)

st.title("LangChain Chatbot")
country = st.text_input("Enter a country")

if country:
    response = model.invoke(prompt.format(country=country, model_name=model.model_name))
    st.write("Answer:\n")
    st.write(response.content)
