# chatbot_v3.py
import streamlit as st
import openai
import time
import os
from utils_pages import change_bg
from src.homepage import display_home
# Setup Page
st.set_page_config(page_title="Home", page_icon = ":one:", layout="wide")
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
    change_bg()
    st.title(":red-background[ :bricks: Material Selection AI :bricks:]")

    with st.container(height = 150):
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

with st.sidebar:
    st.write("")
    page_back, page_forward = st.columns(2, vertical_alignment="center")
    with page_forward:
        if st.button("Next"):
             st.switch_page("pages/2_My_Projects.py")


def main():
    display_home()


if __name__ == "__main__":
    main()
