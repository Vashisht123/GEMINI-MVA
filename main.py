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
st.session_state.setdefault("chat_history", [])
st.session_state.setdefault("last_sent", None)  # Tracks last user message sent

# --- Display chat history ---
def display_chat():
    for role, text in st.session_state["chat_history"]:
        if role == "You":
            st.chat_message("user").markdown(text)
        else:
            st.chat_message("assistant").markdown(f"**{role}:** {text}")

# --- Input box ---
user_input = st.text_input("Type your message here:")

# --- Send button ---
if st.button("Send") and user_input.strip() != "":
    # Only append if this message is new
    if user_input.strip() != st.session_state["last_sent"]:
        st.session_state["chat_history"].append(("You", user_input.strip()))
        st.session_state["last_sent"] = user_input.strip()  # Mark as sent

        display_chat()

        # Typing simulation
        placeholder = st.empty()
        with placeholder.container():
            st.write("🤖 Agent is typing...")

        # Get agent response
        result = coordinator.route(user_input.strip())
        placeholder.empty()

        st.session_state["chat_history"].append((result["agent"], result["text"]))
        display_chat()
