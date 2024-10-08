# chatbot_v3.py
import streamlit as st
import openai
import time
import os
from utils import add_image_from_local, change_bg
from src.homepage import display_home
from src.my_project_page import display_my_projects
from src.chatbot_expanded import display_chatbot_expanded
from src.contacts import display_contacts
from src.showcase import display_showcase


# Setup Page
st.set_page_config(page_title="Bailey Kyle Tang", page_icon = ":skull:", layout="wide")
change_bg('./images/ashgray.png')
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
    st.title(":red-background[ :bricks: Material Selection AI :bricks:]")

    with st.container(height = 135):
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

