

from langchain_ollama import ChatOllama
import streamlit as st


llm = ChatOllama(
    model="gemma3:1b",
    base_url="http://localhost:11434",
)

st.subheader("🤖 Local QnA Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])


query = st.chat_input("Ask anything...")
if query:
    st.chat_message("user").markdown(query)
    st.session_state.messages.append( {"role":"user", "content": query} )

    
    with st.spinner("Generating..."):
        res = llm.invoke(query)
        st.chat_message("ai").markdown(res.content)
    st.session_state.messages.append( {"role":"ai", "content": res.content} )





# while True:
#     query = input("User: ")
#     if query == "quit":
#         break

#     # res = llm.invoke(query)
#     chunks = llm.stream(query)
#     for chunk in chunks:
#         print(chunk.content, end="", flush=True)
#     print("\n")


