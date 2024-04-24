import streamlit as st
import PyPDF2
import google.generativeai as genai

def retrieve_text_from_pdf(pdf):
    with open(pdf, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def main():
    # PDF Path
    pdf = "2404.07143.pdf"
    model = "gemini-1.5-pro-latest"
    with open("apikey.txt", "r") as file:
        key = file.read()
    genai.configure(api_key=key)
    st.title("""The "Leave No Context Behind" paper's RAG System""")
    question = st.text_input("Enter your question: ")

    if st.button("Generate"):
        if question:
            text = retrieve_text_from_pdf(pdf)
            context = text + "\n\n" + question
            ai = genai.GenerativeModel(model_name=model)
            response = ai.generate_content(context)  
            st.subheader("Question:")
            st.write(question)
            st.subheader("Answer:")
            st.write(response.text)
        else:
            st.warning("Please enter your question.")

if __name__ == "__main__":
    main()