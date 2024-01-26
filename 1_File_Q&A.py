import streamlit as st

with st.sidebar:
    anthropic_api_key = st.text_input("Anthropic API Key", key="file_qa_api_key", type="password")
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/1_File_Q%26A.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("📝 File Q&A with OpenAI and Cohere")
uploaded_file = st.file_uploader("Upload an article", type=("txt", "md"))
question = st.text_input(
    "Ask something about the article",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)

col1, col2 = st.columns(2)

#original = Image.open(image)
col1.header("OpenAI GPT-3.5")
col1.write("#### Anthropic Answer")
col2.header("Cohere Command 52B")
col2.write("### Cohere Answer")
#col1.image(original, use_column_width=True)

st.write("### Answer")
#st.write(response.completion)
