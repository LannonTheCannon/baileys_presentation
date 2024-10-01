# chatbot_v3.py
import streamlit as st
import openai
import time
import os
from src.homepage import display_home
from src.my_project_page import display_my_projects
from src.chatbot_expanded import display_chatbot_expanded
from src.contacts import display_contacts
from src.showcase import display_showcase

# Setup Page
st.set_page_config(page_title="Bailey Kyle Tang", page_icon = ":skull:", layout="wide")
ASSISTANT_ID = "asst_I5jUjKMGObw1PnasEbEn2AQ5"
THREAD_ID = "thread_9vkU15hrjp4L4lQYOLKpabrP"

# Openai Client
api_key = st.secrets.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")
if not api_key:
    st.error('OpenAi API Key was not found. Please set it in Streamlit secrets or as an enviromental varible')
    st.stop()
client = openai.OpenAI(api_key=api_key)


# Creating Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# responses
def get_assistant_response(assistant_id,thread_id, user_input):
    try:
        # user message
        client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=user_input
            )

        # Thinking
        run = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id
            )
        
        # Waiting
        while True:
            run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
            if run_status.status == 'completed':
                break
            time.sleep(1)

        # Responses
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        # Latest Response
        return messages.data[0].content[0].text.value
    except Exception as e:
        st.error(f'Error getting assistant reponse: {str(e)}')
        return "I'm sorry, but an error occurred while processing your request."

# Displaying Chat
def display_chatbot():
    st.title(":bricks: Material Selection Ai :bricks:")
    st.header("Purpose")
    st.write("An Ai ment to help mechanical, civil, electerical and any other type of engneering with choosing the right material for their projects.")
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User And Ai responses
    prompt = st.chat_input("Ask me anything!")
    if prompt:
        st.session_state.messages.append({"role":"user","content":prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = get_assistant_response(
                ASSISTANT_ID,
                THREAD_ID,
                prompt
                )
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role":"assistant","content":full_response})

# Display Id
#st.sidebar.write(f'Assistant ID: {ASSISTANT_ID}')
#st.sidebar.write(f'Thread ID: {THREAD_ID}')


def main():
    with st.sidebar:
        #st.image("data:image/jpeg;base64,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")
        st.title(":orange-background[Navigation]")
    sections = [
        ":green-background[Home]", 
        ":blue-background[My projects]",
        ":red-background[Chatbot]",
        ":green-background[Chatbot explained]",
        ":violet-background[Contacts]",
        ":rainbow-background[Project Showcase]"
        ]
    selected_section = st.sidebar.radio('',sections)
    if selected_section == ":green-background[Home]":
        display_home()
    if selected_section == ":blue-background[My projects]":
        display_my_projects()
    if selected_section == ":green-background[Chatbot explained]":
        display_chatbot_expanded()
    if selected_section == ":red-background[Chatbot]":
        display_chatbot()
    if selected_section == ":violet-background[Contacts]":
        display_contacts()
    if selected_section == ":rainbow-background[Project Showcase]":
        display_showcase()

if __name__ == "__main__":
    main()

