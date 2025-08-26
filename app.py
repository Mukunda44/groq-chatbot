import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

langchain_key = st.secrets.get("LANGCHAIN_API_KEY") or os.getenv("LANGCHAIN_API_KEY")

if langchain_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_key
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot with Groq"
else:
    st.error("❌ LANGCHAIN_API_KEY is missing! Add it in Streamlit Secrets or .env file.")

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to user queries."),
        ("user", "Question: {question}")
    ]
)

def generate_response(question, user_groq_key, model_name, temperature, max_tokens):
    """Generates a response using the user's Groq API key."""
    llm = ChatGroq(
        model=model_name,
        groq_api_key=user_groq_key,
        temperature=temperature,
        max_tokens=max_tokens
    )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

# App title
st.title("Enhanced Q&A Chatbot With Groq")

# Sidebar settings
st.sidebar.header("Settings")
user_groq_key = st.sidebar.text_input(
    "Enter your Groq API Key:",
    type="password",
    help="Use your own Groq API key to run the chatbot."
)
model_name = st.sidebar.selectbox("Select a model", ["Llama3-8b-8192", "gemma2-9b-it"])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max-Tokens", min_value=50, max_value=300, value=150)

# Main interface
st.write("Ask any question below:")

user_input = st.text_input("You:")

if user_input:
    if user_groq_key:
        try:
            response = generate_response(user_input, user_groq_key, model_name, temperature, max_tokens)
            st.write("**Chatbot:**", response)
        except Exception as e:
            st.error(f"Error generating response: {e}")
    else:
        st.warning("Please enter your Groq API key in the sidebar first.")
else:
    st.write("Waiting for your question...")

