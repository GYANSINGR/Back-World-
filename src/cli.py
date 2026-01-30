import sys
import os

# Add the project root to sys.path to allow imports from src if run directly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agent import ProblemDiagnosisAgent

def main():
    print("Initializing Problem Diagnosis Agent...")
    try:
        agent = ProblemDiagnosisAgent()
    except ValueError as e:
        print(f"Error: {e}")
        return

    print("\n--- Problem Diagnosis Agent ---")
    print("I am here to identify your real underlying problem.")
    print("Type 'exit' or 'quit' to stop.")
    print("-------------------------------\n")

    print("Agent: Please describe what is on your mind.")

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except EOFError:
            break

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting diagnosis session.")
            break

        if not user_input:
            continue

        response = agent.diagnose(user_input)
        print(f"\nAgent: {response}")

if __name__ == "__main__":
    main()
