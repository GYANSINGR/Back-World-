from src.core.agent import SemaseAgent
from src.prompts import ORCHESTRATOR_PROMPT

class MasterOrchestrator(SemaseAgent):
    def __init__(self, api_key: str = None):
        super().__init__(
            name="Master Orchestrator",
            role="Agent 1: Coordinates agents, decides execution order, detects stagnation.",
            system_prompt=ORCHESTRATOR_PROMPT,
            api_key=api_key
        )
