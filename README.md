# 🧠 Enhanced Q&A Chatbot with Groq & LangChain

This is a **Streamlit-based interactive Q&A chatbot** powered by **Groq LLM models** (via `langchain_groq`) and **LangChain prompt chaining**. Users can supply their **own Groq API key**, select a model, and configure parameters like **temperature** and **max tokens**.

---

## 🚀 Features
- ✅ **Streamlit UI** – Clean and interactive user interface.
- ✅ **Groq API Integration** – Accepts user-provided Groq API key for authentication.
- ✅ **LangChain Prompt Template** – Provides structured reusable prompts.
- ✅ **Customizable Parameters**:
  - Model selection (e.g., `Llama3-8b-8192`, `gemma2-9b-it`)
  - Temperature (creativity control)
  - Max token limit
- ✅ **Environment Variables & Streamlit Secrets** for secure API key management.
- ✅ **LangChain Tracing** support for debugging and analytics.

---

## 📦 Tech Stack
- **Streamlit** – Frontend UI framework
- **LangChain** – Prompt orchestration
- **Groq** – High-performance LLM backend
- **python-dotenv** – For local development with `.env` files

---

## 🛠 Installation & Setup (Local)

### 1. Clone the repository
```bash
git clone https://github.com/Mukunda44/groq-chatbot.git
cd groq-chatbot
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add a `.env` file for local development
```
LANGCHAIN_API_KEY=your_langchain_api_key_here
```

---

## ▶️ Run the Application Locally
```bash
streamlit run app.py
```

---

## 🌐 Deploying on Streamlit Cloud
When deploying to **Streamlit Cloud**, `.env` files are **not uploaded** for security reasons.  
Instead, use **Streamlit Secrets**:

1. Go to **Streamlit → Your App → Settings → Secrets**.
2. Add:
```
LANGCHAIN_API_KEY="your_api_key_here"
```

Your code already supports this with:
```python
langchain_key = st.secrets.get("LANGCHAIN_API_KEY") or os.getenv("LANGCHAIN_API_KEY")
```

This means:
- Locally → uses `.env`
- Streamlit Cloud → uses `st.secrets`

✅ No crashes if the key is missing, it will show a warning instead.

---

## ⚙️ How It Works
1. Enter your **Groq API Key** in the sidebar or configure it via secrets.
2. Select the **model** (e.g., `Llama3-8b-8192`, `gemma2-9b-it`).
3. Adjust **temperature** (controls creativity) and **max tokens** (response length).
4. Ask any question in the text box and get an AI-generated answer.

---

## ✅ Example Usage
**Input:**  
```
What is LangChain?
```
**Output:**  
```
LangChain is a framework for building applications powered by large language models...
```

---

## 🔍 LangChain Tracing
To enable tracing, set these in your `.env` or Streamlit Secrets:
```
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT="Q&A Chatbot with Groq"
```

Track execution details in **LangSmith dashboard**.

---

## 📜 License
MIT License — Free to use, modify, and share.

---

### ✅ Deployment Checklist
✔ Push your code to GitHub  
✔ Add `LANGCHAIN_API_KEY` in Streamlit Secrets  
✔ Run the app on **Streamlit Cloud**  
✔ Enjoy your AI chatbot 🚀

