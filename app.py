import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from langchain_groq.chat_models import ChatGroq
import matplotlib.pyplot as plt
from datetime import datetime
import os
from dotenv import load_dotenv
import io

# Load environment variables
load_dotenv()

# Initialize LLM
api_key = os.getenv('GROQ_API_KEY')
if not api_key:
    st.error("GROQ_API_KEY is not set in the environment variables.")
    st.stop()

llm = ChatGroq(model_name='llama3-70b-8192', api_key=api_key)

# Streamlit interface
st.title("Data Analysis Chatbot")
st.write("Upload your CSV file to analyze the data.")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        df = SmartDataframe(data, config={'llm': llm})
        st.write("Data Preview:")
        st.write(data.head())

        if 'conversation' not in st.session_state:
            st.session_state.conversation = []

        # Display the conversation history
        for q, r in st.session_state.conversation:
            st.write(f"**Q:** {q}")
            if isinstance(r, plt.Figure):
                st.pyplot(r)
            elif isinstance(r, str):
                st.write(f"**A:** {r}")

        # Input for new query
        query = st.text_input("Ask a question about the data:")
        if st.button('Submit', key='submit_query'):
            if query:
                try:
                    response = df.chat(query)
                    # Check if the response is a plot
                    if isinstance(response, plt.Figure):
                        img_buffer = io.BytesIO()
                        response.savefig(img_buffer, format='png')
                        img_buffer.seek(0)
                        st.image(img_buffer, caption='Generated Plot')
                    else:
                        st.write(f"**A:** {response}")
                    st.session_state.conversation.append((query, response))
                except Exception as e:
                    st.error(f"An error occurred while processing your query: {str(e)}")
    except Exception as e:
        st.error(f"An error occurred while reading the file: {str(e)}")
