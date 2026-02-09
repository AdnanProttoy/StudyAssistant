# app.py
import streamlit as st
from helper_bot import get_answer
from readPdf import read_pdf
from imageViewer import read_image_text

st.set_page_config(page_title="Study Helper Chatbot")
st.title("Study Helper Chatbot Designed By PROTTOY")
st.write("Make Your Study Easier 😊")

st.markdown("---") 

st.subheader("Ask a Text Question")
text_question = st.text_input("Write your question here:")

if st.button("Get Answer for Text Question"):
    if text_question.strip():
        answer = get_answer(text_question)
        st.subheader("Answer:")
        st.write(answer)
    else:
        st.warning("Please type a question first!")

st.markdown("---")  

st.subheader("Ask a Question from PDF")
pdf_file = st.file_uploader("Upload your PDF here:", type=["pdf"])

if pdf_file:
    pdf_text = read_pdf(pdf_file)
    pdf_question = st.text_input("Ask a question about the PDF:")

    if st.button("Get Answer for PDF Question"):
        if pdf_question.strip():
            prompt = f"PDF content: {pdf_text}\nQuestion: {pdf_question}"
            answer = get_answer(prompt)
            st.subheader("Answer:")
            st.write(answer)
        else:
            st.warning("Please type a question about the PDF!")

st.markdown("---")  

st.subheader("Ask a Question from Image")
#image_file = st.file_uploader("Upload an image here:", type=["png", "jpg", "jpeg"])

##if image_file:
    #image_text = read_image_text(image_file)
    #image_question = st.text_input("Ask a question about the image:")

    #if st.button("Get Answer for Image Question"):
        #if image_question.strip():
            #prompt = f"Image content: {image_text}\nQuestion: {image_question}"
            #answer = get_answer(prompt)
            #st.subheader("Answer:")
            #st.write(answer)
        #else:
            #st.warning("Please type a question about the image!")


st.subheader("Image-based Question")

image_file = st.file_uploader("Upload an image (PNG/JPG)", type=["png", "jpg", "jpeg"])

image_description = st.text_area(
    "Describe what is written or shown in the image"
)

image_question = st.text_input("What do you want to know from this image?")

if st.button("Answer Image Question"):
    if image_description and image_question:
        prompt = f"""
        The user uploaded an image.
        Image description: {image_description}
        Question: {image_question}
        """
        answer = get_answer(prompt)
        st.write(answer)
    else:
        st.warning("Please describe the image and ask a question.")
