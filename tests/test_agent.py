import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agent import ProblemDiagnosisAgent

class TestProblemDiagnosisAgent(unittest.TestCase):

    def setUp(self):
        # Setup environment variable for testing
        os.environ["GEMINI_API_KEY"] = "test_key"

    @patch("src.agent.genai")
    def test_initialization(self, mock_genai):
        agent = ProblemDiagnosisAgent()

        # Verify configure was called with the key
        mock_genai.configure.assert_called_with(api_key="test_key")

        # Verify model initialization
        mock_genai.GenerativeModel.assert_called()

        # Verify chat session started
        # Depending on how the mock works, accessing agent.model might be accessing the return value of GenerativeModel()
        # So we verify that start_chat was called on the mock object returned by GenerativeModel
        mock_genai.GenerativeModel.return_value.start_chat.assert_called_with(history=[])

    @patch("src.agent.genai")
    def test_initialization_with_explicit_key(self, mock_genai):
        agent = ProblemDiagnosisAgent(api_key="explicit_key")
        mock_genai.configure.assert_called_with(api_key="explicit_key")

    @patch("src.agent.genai")
    def test_diagnose(self, mock_genai):
        agent = ProblemDiagnosisAgent()

        # Mock the response
        mock_chat = agent.chat_session
        mock_response = MagicMock()
        mock_response.text = "Diagnostic response"
        mock_chat.send_message.return_value = mock_response

        response = agent.diagnose("My problem is X")

        mock_chat.send_message.assert_called_with("My problem is X")
        self.assertEqual(response, "Diagnostic response")

    @patch("src.agent.genai")
    def test_error_handling(self, mock_genai):
        agent = ProblemDiagnosisAgent()

        # Mock an exception
        mock_chat = agent.chat_session
        mock_chat.send_message.side_effect = Exception("API Error")

        response = agent.diagnose("My problem is X")

        self.assertIn("Error communicating with the diagnosis agent", response)
        self.assertIn("API Error", response)

    def tearDown(self):
        if "GEMINI_API_KEY" in os.environ:
            del os.environ["GEMINI_API_KEY"]

if __name__ == "__main__":
    unittest.main()
