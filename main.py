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

# --- Session state initialization ---
st.session_state.setdefault("chat_history", [])
st.session_state.setdefault("input", "")

# --- Function to display chat history ---
def display_chat():
    for role, text in st.session_state.chat_history:
        if role == "You":
            st.chat_message("user").markdown(text)
        else:
            st.chat_message("assistant").markdown(f"**{role}:** {text}")

# --- Input box ---
user_input = st.text_input("Type your message here:", key="input")

# --- Handle Send button ---
if st.button("Send") and user_input:
    # Append user message
    st.session_state.chat_history.append(("You", user_input))

    # Clear input safely
    st.session_state["input"] = ""

    display_chat()

    # Typing simulation
    placeholder = st.empty()
    with placeholder.container():
        st.write("🤖 Agent is typing...")

    # Get agent response
    result = coordinator.route(user_input)
    placeholder.empty()

    # Append agent response
    st.session_state.chat_history.append((result["agent"], result["text"]))
    display_chat()
