import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import streamlit as st
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from aux_module import get_raw_text_from_pdfs, get_chunks, process_files, clear_history, create_chunks
from langchain.chains import create_history_aware_retriever
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.vectorstores.chroma import Chroma

env_path = os.path.join(os.getcwd(), '.env')
# loading the environment variables
load_dotenv(dotenv_path=env_path)

print(os.getenv('OPENAI_API_KEY'))
# define the model
llm = "gpt-4o"

model = ChatOpenAI(model=llm, api_key=os.getenv('OPENAI_API_KEY'))

# function
# function that performs the vectorization - embeddings and stores them
# into a vectorstore

def get_vectorstore(txt_chunks):
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv('OPENAI_API_KEY'))
    vectorstore = Chroma.from_documents(txt_chunks, embeddings)
    return vectorstore

system_prompt = (
    "You are an assitant for question-answering tasks."
    "Use the following pieces of retrieved context to answer the user's question."
    "If you don't know the answer, say 'This is not known to me!!!'"
    "Use at most 5 sentences max to answer the question."
    "\n\n"
    "{context}"
)

contextualized_system_prompt = """
Given a chat history and latest user question \
which might reference context in chat history, formulate a standalone question \
which can be understood without the chat history. Do NOT answer zhe question, \
just reformulate it if needed and otherwise return as it is."""

contextualized_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualized_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ]
)

prompt = ChatPromptTemplate(
    [
        ("system", system_prompt),
        ("user", "{input}")
    ]
)



question_answering_chain = create_stuff_documents_chain(model, prompt)


history = StreamlitChatMessageHistory()


# Streamlit part

st.title("Question Answering System")

uploaded_files = st.file_uploader("Upload a file", type=["pdf", "docx", "txt"], accept_multiple_files=True)
add_files = st.button("Submit files", on_click=clear_history)

if uploaded_files and add_files:
    documents = process_files(uploaded_files)
    all_chunks = create_chunks(documents)
    vectorstore = get_vectorstore(all_chunks)
    print("vectorstore created!!!!")
    retriever = vectorstore.as_retriever()
    history_aware_retriever = create_history_aware_retriever(model, retriever, contextualized_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever,question_answering_chain)
    # conversational rag chain 
    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        lambda session_id: history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer"
    )
    st.session_state.crc = conversational_rag_chain
    st.success("Files processed successfully - ready to answer questions")
    


for message in st.session_state["langchain_messages"]:
    role = "user" if message.type == "human" else "assistant"
    with st.chat_message(role):
        st.markdown(message.content)

question = st.text_input("Ask me a question:")

if question:
    with st.chat_message("user"):
        st.markdown(question)
    if "crc" in st.session_state:
        crc = st.session_state["crc"]
        answer_chain = crc.pick("answer")
        response = answer_chain.stream(
            {"input": question},
            config={"configurable": {"session_id": "any"}}
        )
        with st.chat_message("assistant"):
            st.write_stream(response)
    else:
        st.error("Please upload files first")
    