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

# Input box
with st.chat_input("Type your message here...") as user_input:
    if user_input:
        # Add user message
        st.session_state.chat_history.append(("You", user_input))
        display_chat()
        
        # Add typing animation
        placeholder = st.empty()
        with placeholder.container():
            st.chat_message("assistant").markdown("Typing...")

        # Get agent response
        result = coordinator.route(user_input)
        time.sleep(0.5)  # simulate typing delay

        # Remove typing and add real response
        placeholder.empty()
        st.session_state.chat_history.append((result["agent"], result["text"]))
        display_chat()
