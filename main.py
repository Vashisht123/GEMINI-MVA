import streamlit as st
from agents.coordinator import Coordinator
from utils.memory import Memory
import time

# --- Initialize memory and coordinator ---
memory = Memory()
coordinator = Coordinator(memory)

st.set_page_config(
    page_title="Gemini Multi-Agent Assistant",
    layout="centered",
)

st.title("🤖 Gemini Multi-Agent Assistant")

# --- Initialize session state keys ---
st.session_state.setdefault("chat_history", [])
st.session_state.setdefault("input_text", "")

# --- Function to display chat history ---
def display_chat():
    for role, text in st.session_state.chat_history:
        if role == "You":
            st.chat_message("user").markdown(text)
        else:
            st.chat_message("assistant").markdown(f"**{role}:** {text}")

# --- Input box bound to session state ---
user_input = st.text_input("Type your message here:", key="input_text")

# --- Handle Send button safely ---
if st.button("Send") and st.session_state.input_text.strip() != "":
    # Append user message
    st.session_state.chat_history.append(("You", st.session_state.input_text.strip()))

    display_chat()  # show user message immediately

    # Typing simulation
    placeholder = st.empty()
    with placeholder.container():
        st.write("🤖 Agent is typing...")

    # Get agent response from Coordinator
    result = coordinator.route(st.session_state.input_text.strip())
    placeholder.empty()

    # Append agent response
    st.session_state.chat_history.append((result["agent"], result["text"]))

    display_chat()  # show agent response

    # Clear input safely
    st.session_state.input_text = ""
