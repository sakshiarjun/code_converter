import streamlit as st

left,right = st.columns(2,gap="medium")
with left: 
    st.header("Input")
    input_option=st.selectbox("Choose language", ("C","C++","Java"))
    st.text_area("Paste your code here",height = 300)

with right: 
    st.header("Output")
    output_option=st.selectbox("Choose language", ("Python","Java"))
    st.text_area(" ",height = 300)

st.button("Convert")