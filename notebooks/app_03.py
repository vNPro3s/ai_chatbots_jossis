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
    input_variables=["programming_language", "num_paragraphs", "language"],
    template="""Write an essay in {language} language about programming language {programming_language} limmited to {num_paragraphs} paragraphs length.
    Specialy, for nonexistent programming languages, provide only response in the form of the message '{programming_language} is fictional'.
    programming language'.
    You must include the name of at least one person who has contributed to the development of the programming language, 
and the year the programming language was first released. IMORTANT: Each paragraph should have at least 5 sentences.""")
    
st.title("LangChain Chatbot")

prog_lang = st.text_input("Enter a programming language.")
num_par = st.number_input("Enter the number of paragraphs.", min_value=1, max_value=5)
language = st.text_input("Enter a language for an essay.")

if prog_lang and num_par and language:
    response = model.invoke(prompt.format(programming_language=prog_lang, num_paragraphs=num_par, language=language))
    st.write("Answer:\n")
    st.write(response.content)