
import streamlit as st
import os
from google import genai

# Load API Key securely
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("Please set GOOGLE_API_KEY in environment variables")
    st.stop()

# Initialize client
client = genai.Client(api_key=api_key)

# UI
st.title("Ask Me Anything 🚀")

with st.form('my_form'):
    text = st.text_input('Enter your question:')
    submit = st.form_submit_button('Ask')

if submit:
    if text.strip():
        with st.spinner("Thinking..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=text
                )

                #st.success("Response:")
                st.write(response.text)

            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a question!")
