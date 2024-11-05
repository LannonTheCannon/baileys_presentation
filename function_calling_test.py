# function_calling_test.py
import openai
import streamlit as st
import json
import time

api_key = st.secrets["OPENAI_API_KEY"] 
client = openai.OpenAI(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "assistant_id" not in st.session_state:
    st.session_state.assistant_id = ""
    st.session_state.asssitant_id = "asst_VfgjLDxvMm6GVez3Epzku4TU"

if "thread_id" not in st.session_state:
    st.session.state.thread_id = ""
    st.session_state.thread_id = "thread_ABczMIxnXlYXRpxSlUS5vyqC"
def  get_current_tempature(location: str,unit: str) -> str:
    
    return f'75*{unit[0]}'

def get_assistant_response(assistant_id, thread_id, user_input):
    try:
        client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=user_input
        )
        run = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id,
            tools=[
                {
                    "type":"function",
                    "name":"get_current_tempature",
                    "function":{
                        "description":"Get the current tempature for a specific location",
                        "strict":True,
                        "parameters":{
                            "location":{
                                "type":"string",
                                "description":"The city and state, e.g San Francisco, CA"
                            },
                            "units":{
                                "type":"string",
                                "enum":["Celsius, Fahreheit"],
                                "description":"The tempeature unit to use"
                            }
                        },
                        "required":["location","unit"]
                    }
                }
            ]
        )

        while True:
            run_status = client.beta.threads.runs.retrive(
                thread_id=thread_id,
                run_id=run.d
            )
            if run_status.status == "completed":
                break
            elif run_status.status == "require_action":
                tool_outputs = []
                for tool_call in run_status.required_action.submit_tool_output.tool_calls:
                    if tool_call.function.name == "get_current_tempature":
                        arguments = json.loads(tool_call.function.arguments)
                        tempature = get_current_tempature(
                            location=arguments["location"],
                            unit=arguments["unit"]
                        )
                        tool_outputs.append({
                            "tool_call_id":tool_call.id,
                            "output":json.dumps({
                                "temprature":temprature
                                })
                        })
                client.beta.threads.runs.submit_tool_outputs(
                    thread_id=thread_id,
                    run_id=run.id,
                    tool_output=tool_outputs
                )
            time.sleep(1)
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        return messages.data[0].content.text.value
    except Exception as e:
        st.error(f'Error getting assistant response: {str({e})}')
        return "I apologize, but I encountered an error, Please try again"


def main():
    st.title("Weather assistant")
    

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    prompt = st.chat_input("Ask me about the weather")
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
        
if __name__ == "__main__":
    main()

    
