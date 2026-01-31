from src.core.agent import SemaseAgent
from src.prompts import SCANNER_PROMPT

class RealWorldScanner(SemaseAgent):
    def __init__(self, api_key: str = None):
        super().__init__(
            name="Real-World Problem & Opportunity Scanner",
            role="Agent 2: Identifies unsolved or poorly solved real-world problems. Frames problems as SYSTEM FAILURES.",
            system_prompt=SCANNER_PROMPT,
            api_key=api_key
        )
