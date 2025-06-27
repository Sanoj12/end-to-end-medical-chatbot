
import streamlit as st
from src.agent import run_agent

from prometheus_client import Counter, start_http_server

CHAT_COUNTER = Counter("chat_total", "Total requests")

###streamlit

st.set_page_config(page_title='Medical Assistant',layout='centered')
st.title("Medical Assistant")


user_input = st.text_area("ask a medical question(in any language)",height=150)


if st.button("Submit"):
    if not user_input.strip():
        CHAT_COUNTER.inc() ##CHAT COUNT
        st.warning("please ask question")

    
    else:
        with st.spinner("Analyzing..."):
            try:
                result= run_agent(user_input)
                st.success("Answer:")
                st.write(result)

            except Exception as e:
                st.error(e)