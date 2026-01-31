import os
import google.generativeai as genai
from abc import ABC, abstractmethod

class SemaseAgent(ABC):
    def __init__(self, name: str, role: str, system_prompt: str, api_key: str = None, model_name: str = "gemini-1.5-flash"):
        self.name = name
        self.role = role
        self.system_prompt = system_prompt
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
             raise ValueError("GEMINI_API_KEY is not set. Please set it in environment variables or pass it to the constructor.")

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name=model_name,
            system_instruction=self.system_prompt
        )
        self.chat_session = self.model.start_chat(history=[])

    def execute(self, user_input: str) -> str:
        """
        Sends user input to the agent and returns the response.
        """
        try:
            response = self.chat_session.send_message(user_input)
            return response.text
        except Exception as e:
            return f"Error executing {self.name}: {str(e)}"

    def reset_session(self):
        self.chat_session = self.model.start_chat(history=[])
