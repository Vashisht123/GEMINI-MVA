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

# --- Initialize chat history ---
st.session_state.setdefault("chat_history", [])

# --- Display chat history ---
def display_chat():
    for role, text in st.session_state["chat_history"]:
        if role == "You":
            st.chat_message("user").markdown(text)
        else:
            st.chat_message("assistant").markdown(f"**{role}:** {text}")

display_chat()

# --- Use form to handle input safely ---
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message here:")
    submitted = st.form_submit_button("Send")

    if submitted and user_input.strip() != "":
        # Append user message
        st.session_state["chat_history"].append(("You", user_input.strip()))
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
