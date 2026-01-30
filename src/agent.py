import os
import google.generativeai as genai
from src.prompts import DIAGNOSIS_SYSTEM_PROMPT

class ProblemDiagnosisAgent:
    def __init__(self, api_key: str = None, model_name: str = "gemini-1.5-flash"):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is not set. Please set it in environment variables or pass it to the constructor.")

        genai.configure(api_key=self.api_key)

        # Initialize model with system instruction
        self.model = genai.GenerativeModel(
            model_name=model_name,
            system_instruction=DIAGNOSIS_SYSTEM_PROMPT
        )
        self.chat_session = self.model.start_chat(history=[])

    def diagnose(self, user_input: str) -> str:
        """
        Sends user input to the agent and returns the diagnostic response.
        """
        try:
            response = self.chat_session.send_message(user_input)
            return response.text
        except Exception as e:
            # In a real backend, we might log this error.
            # Returning the error message to the user/cli for visibility.
            return f"Error communicating with the diagnosis agent: {str(e)}"

    def reset_session(self):
        """Resets the diagnostic session."""
        self.chat_session = self.model.start_chat(history=[])
