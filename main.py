from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()

class ConversationalAssistant:
    def __init__(self, messages):
        self.memory = messages  # Reference to session state messages
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant."),
            MessagesPlaceholder(variable_name="history"),
            ("user", "{input}")
        ])
        self.model = ChatGroq(temperature=0.7)
        self.chain = self.prompt | self.model | StrOutputParser()

    def get_response_generator(self, input_text):
        """Return the LangChain stream generator directly"""
        history_messages = self.memory[:-1]  # All messages except the last one
        history = [(msg["role"], msg["content"]) for msg in history_messages]
        
        return self.chain.stream({
            "input": input_text, 
            "history": history  
        })

class ChatInterface:
    def __init__(self):
        self.initialize_session()
        self.assistant = ConversationalAssistant(st.session_state.messages)

    def initialize_session(self):
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def display_history(self):
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).markdown(msg["content"])

    def handle_input(self):
        if user_input := st.chat_input("Type your message..."):
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.chat_message("user").markdown(user_input)
            
            with st.chat_message("assistant"):
                # Get the generator from LangChain directly
                generator = self.assistant.get_response_generator(user_input)
                
                # Stream the response and capture it
                full_response = st.write_stream(generator)
                
                # Store complete response in memory
                self.assistant.memory.append({
                    "role": "assistant",
                    "content": full_response
                })

    def run(self):
        st.title("Chat Assistant")
        self.display_history()
        self.handle_input()

if __name__ == "__main__":
    ChatInterface().run()