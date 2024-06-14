# pip install openai
import streamlit as st
import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.org_id = os.getenv('ORG_ID')

left,right = st.columns(2,gap="medium")
with left: 
    st.header("Input")
    input_option=st.selectbox("Choose language", ("Python","JavaScript","Java","C++","C#","Ruby","PHP","Swift","Kotlin","Go (Golang)","R","Objective-C","TypeScript","MATLAB","SQL"), key="input_1")
    input_code = st.text_area("Paste your code here",height = 300)

with right: 
    st.header("Output")
    output_option=st.selectbox("Choose language", ("Python","JavaScript","Java","C++","C#","Ruby","PHP","Swift","Kotlin","Go (Golang)","R","Objective-C","TypeScript","MATLAB","SQL"), key="output_2")

prompt = f"can you convert the given code into a valid and working {output_option} code with correct syntax. If there are any errors in the input code, display the error in comment format in the output code\ {input_code}"

client = OpenAI(organization=openai.org_id)
def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

with right:
    st.code(chat_with_gpt(prompt),language='{output_option}')
