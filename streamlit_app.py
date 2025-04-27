import streamlit as st
import time
from nina_chain import chat_with_nina, initialize_nina

st.set_page_config(page_title="Nina - Structured Case Assistant", page_icon="🕸️")

# Initialize memory on first run
if "initialized" not in st.session_state:
    intro_message = initialize_nina()
    st.session_state.initialized = True
    st.session_state.messages = [{"role": "nina", "content": intro_message}]
    st.session_state.input_text = ""  # initialize input field

# Display chat history
st.title("🕸️ Nina - Structured Justice for Scam Victims")

# Display chat history first
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**Nina:** {message['content']}")

# Display in-progress streaming reply, if any
if st.session_state.get("streaming_reply"):
    st.markdown(f"**Nina:** {st.session_state.streaming_reply}")

# User input field
user_input = st.text_input(
    "Tell Nina what happened to you...",
    key="input_text",
    placeholder="Type your message and press Enter...",
    on_change=lambda: send_message()
)

# Define sending logic separately
def send_message():
    user_message = st.session_state.input_text.strip()

    if user_message:
        # Save user's message
        st.session_state.messages.append({"role": "user", "content": user_message})

        # Initialize temporary streamed reply
        st.session_state.streaming_reply = ""

        # Streaming response
        for chunk in chat_with_nina(user_message, st.session_state.messages, stream=True):
            if chunk:
                st.session_state.streaming_reply += chunk

        # Save full Nina reply to messages
        st.session_state.messages.append({"role": "nina", "content": st.session_state.streaming_reply})

        # Clear temporary streamed reply after it's saved
        st.session_state.streaming_reply = None

        # Clear input field
        st.session_state.input_text = ""

# Footer
st.caption("Data structured with care, powered by FiCAP. Structured truth defeats organized deception.")