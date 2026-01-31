import unittest
from unittest.mock import patch, MagicMock
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.engine import SemaseEngine

class TestSemaseEngine(unittest.TestCase):
    def setUp(self):
        os.environ["GEMINI_API_KEY"] = "test_key"

    @patch("src.core.agent.genai")
    def test_initialization(self, mock_genai):
        engine = SemaseEngine()
        self.assertIsNotNone(engine.orchestrator)
        self.assertIsNotNone(engine.scanner)

    @patch("src.core.agent.genai")
    def test_process_input_delegation(self, mock_genai):
        engine = SemaseEngine()

        # Mock Orchestrator response to trigger Scanner
        mock_orch_chat = engine.orchestrator.chat_session
        mock_orch_response = MagicMock()
        mock_orch_response.text = "I will delegate this to Agent 2 (Scanner) to diagnose the problem."
        mock_orch_chat.send_message.return_value = mock_orch_response

        # Mock Scanner response
        mock_scan_chat = engine.scanner.chat_session
        mock_scan_response = MagicMock()
        mock_scan_response.text = "Scanner Analysis: System Failure Detected."
        mock_scan_chat.send_message.return_value = mock_scan_response

        output = engine.process_input("My system is broken.")

        self.assertIn("--- Orchestrator Plan ---", output)
        self.assertIn("--- Scanner Output ---", output)
        self.assertIn("Scanner Analysis: System Failure Detected.", output)

    @patch("src.core.agent.genai")
    def test_process_input_no_delegation(self, mock_genai):
        engine = SemaseEngine()

        # Mock Orchestrator response NOT triggering Scanner
        mock_orch_chat = engine.orchestrator.chat_session
        mock_orch_response = MagicMock()
        mock_orch_response.text = "I need more information. Please clarify."
        mock_orch_chat.send_message.return_value = mock_orch_response

        output = engine.process_input("Hello.")

        self.assertIn("--- Orchestrator Plan ---", output)
        self.assertNotIn("--- Scanner Output ---", output)

    def tearDown(self):
        if "GEMINI_API_KEY" in os.environ:
            del os.environ["GEMINI_API_KEY"]

if __name__ == "__main__":
    unittest.main()
