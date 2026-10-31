import streamlit as st
import anthropic

client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

st.title("Claude-like Clone 🐙")

if "messages" not in st.session_state:
      st.session_state.messages = []

for message in st.session_state.messages:
      with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt:= st.chat_input("Ask a question..."):
      with st.chat_message("user"):
            st.markdown(prompt)
      st.session_state.messages.append({"role":"user", "content":prompt})

      with st.chat_message("assistant"):
            with client.messages.stream(model="claude-haiku-5-5", max_tokens=1000, messages=st.session_state.messages) as stream:
                  response = st.write_stream(stream.text_stream)
      st.session_state.messages.append({"role":"assistant", "content":response})