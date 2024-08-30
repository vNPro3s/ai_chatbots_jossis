import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st

env_path = os.path.join(os.getcwd(), '.env')
# loading the environment variables
load_dotenv(dotenv_path=env_path)

print(os.getenv('OPENAI_API_KEY'))
# define the model
llm = "gpt-4o"


model = ChatOpenAI(model=llm, api_key=os.getenv('OPENAI_API_KEY'))

st.title("LangChain Chatbot")

question = st.text_input("Ask me anything")

if question:
    response = model.invoke(question)
    st.write(response.content)
    
    
