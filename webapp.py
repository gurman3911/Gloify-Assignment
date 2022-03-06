from ast import keyword
import streamlit as st
from mainModel import gpt3

st.title("Headlines Generator")

st.warning('this is made for assignment provided by the Pragmatic Leaders for the intership only')

st.write('This A.I. program is made to generate Text output with right grammer and punctuations when a input is provided by the user')
st.caption('The Davinci-001 api is used to complete or generate the set of text as per input')

content = st.text_input("Sentense you want to fix")
result = gpt3(content)

if st.button('show results'):
    st.write(result)
    st.success("The program wroked sucessfully")
