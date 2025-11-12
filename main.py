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

# --- Initialize session state ---
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""

# --- Input box bound to session state ---
user_input = st.text_input("Type your message here:", key="user_input")

# --- Send button handler ---
if st.button("Send") and st.session_state.user_input.strip() != "":
    # Append user message once
    st.session_state.chat_history.append(("You", st.session_state.user_input.strip()))

    # Typing simulation
    placeholder = st.empty()
    with placeholder.container():
        st.write("🤖 Agent is typing...")

    # Get agent response
    result = coordinator.route(st.session_state.user_input.strip())
    placeholder.empty()

    # Append agent response
    st.session_state.chat_history.append((result["agent"], result["text"]))

    # Clear input safely by resetting session state key
    st.session_state.user_input = ""

# --- Display chat history ---
for role, text in st.session_state.chat_history:
    if role == "You":
        st.chat_message("user").markdown(text)
    else:
        st.chat_message("assistant").markdown(f"**{role}:** {text}")
