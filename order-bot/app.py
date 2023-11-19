import streamlit as st
import orderBot
import chatgpt

st.title("Order Bot")

if "messages" not in st.session_state:
    st.session_state.messages = orderBot.context

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Place your order"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    response = chatgpt.get_completion_from_messages(st.session_state.messages)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
