# ​ Enhanced Q&A Chatbot with Groq & LangChain

This repository hosts a **Streamlit-based interactive Q&A chatbot** that integrates **Groq LLM models** via `langchain_groq` and **LangChain** for prompt chaining. Users can supply their **own Groq API key**, pick a model, and tweak parameters like **temperature** and **max tokens**.

---

##  Project Overview

Located in the `main` branch, the repository currently includes:
- `app.py` — Core Streamlit application.
- `requirements.txt` — Project dependencies list.
*(As seen on GitHub: Mukunda44/groq-chatbot)* :contentReference[oaicite:0]{index=0}

Currently, it has **0 stars** and **0 forks**, and uses **100% Python**. :contentReference[oaicite:1]{index=1}

---

##  Features
- **Streamlit UI** — Clean and user-friendly interface.
- **Groq API Integration** — Accepts user-supplied Groq API key for authentication.
- **LangChain Prompt Chaining** — Structured templated prompts for consistency.
- **Customizable Parameters**:
  - Model selection (e.g., `Llama3-8b-8192`, `gemma2-9b-it`)
  - Temperature (controls creativity)
  - Max tokens (response length)
- **Environment Variables via `.env`** for LangChain tracing.

---

##  Tech Stack
- **Streamlit** — UI framework.
- **LangChain** — Prompt orchestration.
- **Groq** — High-performance LLM backend.
- **python-dotenv** — Secure environment variable handling.

---

##  Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Mukunda44/groq-chatbot.git
cd groq-chatbot
```

### 2. Set up virtual environment
```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add `.env` file
```env
LANGCHAIN_API_KEY=your_langchain_api_key
# Optional tracing logs
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=Q&A Chatbot with Groq
```

---

##  Running the App
```bash
streamlit run app.py
```
Then, in the web UI:
1. Paste your Groq API key in the sidebar.
2. Choose a model.
3. Set temperature and max tokens.
4. Enter your question and receive the chatbot’s response via Streamlit → LangChain → Groq.

---

##  Example
- **Input:** “What is LangChain?”
- **Output:** A descriptive answer powered by Groq, orchestrated via LangChain.

---

##  License
MIT License — Feel free to use, modify, and redistribute.

---

##  Live Project Info
This project currently has **0 stars**, **0 forks**, and **100% Python code**, with two main files (`app.py` and `requirements.txt`) available. :contentReference[oaicite:2]{index=2}

