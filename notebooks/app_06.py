import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
import streamlit as st
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

env_path = os.path.join(os.getcwd(), '.env')
# loading the environment variables
load_dotenv(dotenv_path=env_path)

print(os.getenv('OPENAI_API_KEY'))
# define the model
llm = "gpt-4o"

model = ChatOpenAI(model=llm, api_key=os.getenv('OPENAI_API_KEY'))

user_prompt = ChatPromptTemplate.from_messages(
    
    messages=[
        ("system",
        "You are an expert that answers questions about various topics. Try to provide a non-detailed answer to the question."),
        
        MessagesPlaceholder(variable_name="chat history"),
        ("human", "{input}")
    ]
    
)

chain = user_prompt | model
history = StreamlitChatMessageHistory()

chain_with_history = RunnableWithMessageHistory(
    chain, 
    lambda session_id: history,
    input_messages_key="input",
    history_messages_key="chat history"
    )


st.title("LangChain Chatbot")

question = st.text_input("Enter a question.")

if question:
    response = chain_with_history.invoke(
        {"input": question},
        config={"session_id": "any"})
    st.write(response.content)
    st.write("Chat history:\n")
    for message in st.session_state["langchain_messages"]:
        if message.type == "human":
            st.write(f"Q: {message.content}")
        else:
            st.write(f"A: {message.content}")