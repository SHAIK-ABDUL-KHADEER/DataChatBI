# import streamlit as st
# import pandas as pd
# from pandasai import SmartDataframe
# from langchain_groq.chat_models import ChatGroq
# import matplotlib.pyplot as plt
# from datetime import datetime
# import os

# # Initialize LLM and read the data
# api_key = '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'
# llm = ChatGroq(model_name='llama3-70b-8192', api_key=api_key)

# # Streamlit interface
# st.title("Data Analysis Chatbot")
# st.write("Upload your CSV file to analyze the data.")

# uploaded_file = st.file_uploader("Choose a file")

# if uploaded_file is not None:
#     data = pd.read_csv(uploaded_file)
#     df = SmartDataframe(data, config={'llm': llm})
#     st.write("Data Preview:")
#     st.write(data.head())

#     if 'conversation' not in st.session_state:
#         st.session_state.conversation = []

#     # Display the conversation history
#     for q, r in st.session_state.conversation:
#         st.write(f"**Q:** {q}")
#         if isinstance(r, plt.Figure):
#             st.pyplot(r)
#         elif isinstance(r, str) and r.startswith('generated_images/'):  # Check if the response is a file path
#             st.image(r)
#         else:
#             st.write(f"**A:** {r}")

#     # Input for new query
#     query = st.text_input("Ask a question about the data:")

#     if st.button('Submit', key='submit_query'):
#         if query:
#             response = df.chat(query)

#             # Check if the response is a plot and needs saving
#             if isinstance(response, plt.Figure):
#                 timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#                 image_path = f"generated_images/response_{timestamp}.png"
#                 os.makedirs("generated_images", exist_ok=True)
#                 response.savefig(image_path)
#                 response = image_path  # Update the response to the image path
#             elif response == '/content/exports/charts/temp_chart.png':
#                 timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#                 image_path = f"generated_images/response_{timestamp}.png"
#                 os.makedirs("generated_images", exist_ok=True)
#                 os.rename('/content/exports/charts/temp_chart.png', image_path)
#                 response = image_path

#             st.session_state.conversation.append((query, response))
#             st.experimental_rerun()
# import streamlit as st
# import pandas as pd
# from pandasai import SmartDataframe
# from langchain_groq.chat_models import ChatGroq
# import matplotlib.pyplot as plt
# from datetime import datetime
# import os

# # Initialize LLM and read the data
# api_key = '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'
# llm = ChatGroq(model_name='llama3-70b-8192', api_key=api_key)

# # Streamlit interface
# st.title("Data Analysis Chatbot")
# st.write("Upload your CSV file to analyze the data.")

# uploaded_file = st.file_uploader("Choose a file")

# if uploaded_file is not None:
#     data = pd.read_csv(uploaded_file)
#     df = SmartDataframe(data, config={'llm': llm})
#     st.write("Data Preview:")
#     st.write(data.head())

#     if 'conversation' not in st.session_state:
#         st.session_state.conversation = []

#     # Display the conversation history
#     for q, r in st.session_state.conversation:
#         st.write(f"**Q:** {q}")
#         if isinstance(r, plt.Figure):
#             st.pyplot(r)
#         elif isinstance(r, str) and r.startswith('generated_images/'):  # Check if the response is a file path
#             st.image(r)
#         else:
#             st.write(f"**A:** {r}")

#     # Input for new query
#     query = st.text_input("Ask a question about the data:")

#     if st.button('Submit', key='submit_query'):
#         if query:
#             response = df.chat(query)

#             # Check if the response is a plot and needs saving
#             if isinstance(response, plt.Figure):
#                 timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#                 image_path = f"generated_images/response_{timestamp}.png"
#                 os.makedirs("generated_images", exist_ok=True)
#                 response.savefig(image_path)
#                 response = image_path  # Update the response to the image path

#             # Append new query and response to the conversation
#             st.session_state.conversation.append((query, response))
#             st.experimental_rerun()

#     # After rerun, display the entire conversation history including the newly added entry
#     if 'conversation' in st.session_state:
#         for q, r in st.session_state.conversation:
#             st.write(f"**Q:** {q}")
#             if isinstance(r, plt.Figure):
#                 st.pyplot(r)
#             elif isinstance(r, str) and r.startswith('generated_images/'):
#                 st.image(r)
#             else:
#                 st.write(f"**A:** {r}")
# import streamlit as st
# import pandas as pd
# from pandasai import SmartDataframe
# from langchain_groq.chat_models import ChatGroq
# import matplotlib.pyplot as plt
# import io
# import os

# # Initialize LLM and read the data
# api_key = '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'
# llm = ChatGroq(model_name='llama3-70b-8192', api_key=api_key)

# # Streamlit interface
# st.title("Data Analysis Chatbot")
# st.write("Upload your CSV file to analyze the data.")

# uploaded_file = st.file_uploader("Choose a file")

# if uploaded_file is not None:
#     data = pd.read_csv(uploaded_file)
#     df = SmartDataframe(data, config={'llm': llm})
#     st.write("Data Preview:")
#     st.write(data.head())

#     if 'conversation' not in st.session_state:
#         st.session_state.conversation = []

#     # Display the conversation history
#     for q, r in st.session_state.conversation:
#         st.write(f"**Q:** {q}")
#         if isinstance(r, bytes):  # If the response is image data in bytes
#             st.image(r)  # Display the image directly
#         else:
#             st.write(f"**A:** {r}")

#     # Input for new query
#     query = st.text_input("Ask a question about the data:")

#     if st.button('Submit', key='submit_query'):
#         if query:
#             response = df.chat(query)

#             # Check if the response is a plot and needs to be converted to image bytes
#             if isinstance(response, plt.Figure):
#                 buf = io.BytesIO()  # Create an in-memory buffer
#                 response.savefig(buf, format='png')  # Save the figure to the buffer
#                 buf.seek(0)  # Rewind the buffer to the beginning
#                 response = buf.getvalue()  # Get the image data as bytes
#                 response.close()  # Close the buffer

#             # Append new query and response to the conversation
#             st.session_state.conversation.append((query, response))
#             st.experimental_rerun()  # Refresh to show new conversation
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from langchain_groq.chat_models import ChatGroq
import matplotlib.pyplot as plt
from datetime import datetime
import io
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Initialize Cloudinary with your credentials
cloudinary.config(
    cloud_name='dmtovhjl2',  # Replace with your cloud name
    api_key='437567415639991',        # Replace with your API key
    api_secret='437567415639991'   # Replace with your API secret
)

# Initialize LLM and read the data
api_key = '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'
llm = ChatGroq(model_name='llama3-70b-8192', api_key=api_key)

def upload_to_cloudinary(image_bytes):
    try:
        response = cloudinary.uploader.upload(image_bytes, folder='streamlit_app', use_filename=True)
        if response and 'url' in response:
            return response['url']
    except Exception as e:
        st.error(f"Failed to upload image to Cloudinary: {e}")
    return None

# Streamlit interface
st.title("Data Analysis Chatbot")
st.write("Upload your CSV file to analyze the data.")
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    df = SmartDataframe(data, config={'llm': llm})
    st.write("Data Preview:")
    st.write(data.head())

    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    # Display the conversation history
    for q, r in st.session_state.conversation:
        st.write(f"**Q:** {q}")
        if isinstance(r, str) and r.startswith('http'):  # If the response is an image URL
            st.image(r, caption='Generated Image')  # Display the image directly from the URL
        else:
            st.write(f"**A:** {r}")

    # Input for new query
    query = st.text_input("Ask a question about the data:")

    if st.button('Submit', key='submit_query'):
        if query:
            response = df.chat(query)

            # Check if the response is a plot and needs to be uploaded
            if isinstance(response, plt.Figure):
                buf = io.BytesIO()  # Create an in-memory buffer
                response.savefig(buf, format='png')  # Save the figure to the buffer
                buf.seek(0)  # Rewind the buffer to the beginning
                image_bytes = buf.getvalue()  # Get the image data as bytes
                buf.close()  # Close the buffer

                # Upload image to Cloudinary and get the URL
                cloudinary_url = upload_to_cloudinary(image_bytes)
                if cloudinary_url:
                    response = cloudinary_url  # Update the response to the Cloudinary URL

            # Append new query and response to the conversation
            st.session_state.conversation.append((query, response))
            st.experimental_rerun()  # Refresh to show new conversation
