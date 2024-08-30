import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain import hub

env_path = os.path.join(os.getcwd(), '.env')
# loading the environment variables
load_dotenv(dotenv_path=env_path)

print(os.getenv('OPENAI_API_KEY'))
# define the model
llm = "gpt-4o"

model = ChatOpenAI(model=llm, api_key=os.getenv('OPENAI_API_KEY'))

# see https://smith.langchain.com/hub
prompt = hub.pull("hwchase17/react")

tools = load_tools(["wikipedia", "ddg-search", "llm-math"], model)

agent = create_react_agent(model, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, handle_parsing_errors=True)

st.title("AI Agent")

question = st.chat_input("Give me a task: ")
if question:
    st.write(llm)
    with st.chat_message("user"):
        st.markdown(question)
    with st.chat_message("assistant"):
        for response in agent_executor.stream({"input": question}):
            # Agent Action
            if "actions" in response:
                for action in response["actions"]:
                    st.write(f"Calling Tool: `{action.tool}` with input `{action.tool_input}`")
            # Observation
            elif "steps" in response:
                for step in response["steps"]:
                    st.write(f"Tool Result: `{step.observation}`")
            # Final result
            elif "output" in response:
                st.write(f'Final Output: {response["output"]}')
            else:
                raise ValueError()
            st.write("---")