import streamlit as st
import google.generativeai as genai
from PIL import Image
from prompts import SYSTEM_PROMPT

# App Title
st.title("MacroSnap AI Nutritionist")

# Access Gemini API Key from Streamlit Secrets
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# File uploader for food images
uploaded_file = st.file_uploader("Choose a food image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Analyze Food"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        with st.spinner("Analyzing..."):
            response = model.generate_content([SYSTEM_PROMPT, image])
            st.subheader("Analysis Result:")
            st.write(response.text)
