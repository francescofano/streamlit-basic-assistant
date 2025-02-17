# Streamlit Chat Assistant with Groq

A modern chat interface built with Streamlit and LangChain, leveraging Groq's powerful LLM API for fast and efficient responses.

## 🌟 Features

- 💬 Real-time chat interface with streaming responses
- 🧠 Conversation memory to maintain context
- 🚀 Powered by Groq's high-performance LLM
- 📝 Markdown support for formatted responses
- 🔄 Session-based conversation history

## 🛠️ Prerequisites

- Python 3.12 or higher
- Groq API key
- LangChain API key (for tracing)

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/francescofano/streamlit-basic-assistant
   cd streamlit-basic-assistant
   ```

2. Create and activate a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   - Copy `.env.example` to `.env`
   - Fill in your API keys:
     ```
     LANGCHAIN_TRACING_V2=true
     LANGCHAIN_API_KEY=your_langchain_api_key_here
     GROQ_API_KEY=your_groq_api_key_here
     ```

## 🚀 Usage

1. Make sure your virtual environment is activated:
   ```bash
   # On Windows
   .\venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

2. Start the Streamlit application:
   ```bash
   streamlit run main.py
   ```

3. Open your web browser and navigate to `http://localhost:8501`
4. Start chatting with the AI assistant!
