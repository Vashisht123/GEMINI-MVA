import streamlit as st
from agents.coordinator import Coordinator
from utils.memory import Memory
import time

# Initialize memory and coordinator
memory = Memory()
coordinator = Coordinator(memory)

st.set_page_config(
    page_title="Gemini Multi-Agent Assistant",
    layout="centered",
)

st.title("🤖 Gemini Multi-Agent Assistant")

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Function to display chat history
def display_chat():
    for msg in st.session_state.chat_history:
        role, text = msg
        if role == "You":
            st.chat_message("user").markdown(text)
        else:
            st.chat_message("assistant").markdown(f"**{role}:** {text}")

# Input boX

user_input = st.text_input("Type your message here:", key="input")

# Only append if Send button is clicked
if st.button("Send") and user_input:
    # Add user message once
    st.session_state.chat_history.append(("You", user_input))
    
    # Clear input box after sending
    st.session_state.input = ""  

    display_chat()

    # Typing simulation
    placeholder = st.empty()
    with placeholder.container():
        st.write("🤖 Agent is typing...")

    # Get agent response
    result = coordinator.route(user_input)
    placeholder.empty()
    st.session_state.chat_history.append((result["agent"], result["text"]))
    display_chat()
