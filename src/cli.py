import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.engine import SemaseEngine

def main():
    print("Initializing SE-MASE (Self-Evolving Multi-Agent Skill Engine)...")
    try:
        engine = SemaseEngine()
    except ValueError as e:
        print(f"Error: {e}")
        return

    print("\n--- SE-MASE ACTIVE ---")
    print("Type 'exit' or 'quit' to stop.")
    print("-------------------------------\n")

    print("Orchestrator: Ready. Awaiting System Input.")

    while True:
        try:
            user_input = input("\nUser (Architect): ").strip()
        except EOFError:
            break

        if user_input.lower() in ["exit", "quit"]:
            print("Shutting down SE-MASE.")
            break

        if not user_input:
            continue

        response = engine.process_input(user_input)
        print(f"\n{response}")

if __name__ == "__main__":
    main()
