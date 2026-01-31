import os
from src.agents.orchestrator import MasterOrchestrator
from src.agents.scanner import RealWorldScanner

class SemaseEngine:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
             raise ValueError("GEMINI_API_KEY is not set.")

        self.orchestrator = MasterOrchestrator(api_key=self.api_key)
        self.scanner = RealWorldScanner(api_key=self.api_key)
        # Initialize other agents as needed

    def process_input(self, user_input: str) -> str:
        """
        Runs the SE-MASE execution loop for a given user input.
        """
        # 1. Diagnose current system-building stage
        # 2. Activate minimum required agents

        # For this prototype, we will let the Orchestrator decide what to do.
        # We pass the user input to the Orchestrator.

        orchestration_plan = self.orchestrator.execute(f"User Input: {user_input}\n\nDecide next steps.")

        # In a full system, we would parse the orchestration_plan and call other agents.
        # For now, we'll assume the Orchestrator might delegate to the Scanner if it detects a problem statement.

        # Simple heuristic for this prototype:
        # If the orchestration plan mentions "Agent 2" or "Scanner", we invoke the scanner.
        output = f"--- Orchestrator Plan ---\n{orchestration_plan}\n"

        if "Agent 2" in orchestration_plan or "Scanner" in orchestration_plan or "diagnose" in orchestration_plan.lower():
             scanner_output = self.scanner.execute(user_input)
             output += f"\n--- Scanner Output ---\n{scanner_output}\n"

        return output

    def reset(self):
        self.orchestrator.reset_session()
        self.scanner.reset_session()
