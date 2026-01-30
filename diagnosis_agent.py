import os
import google.generativeai as genai
import sys

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("Please set it using: export GEMINI_API_KEY='your_key'")
        sys.exit(1)

    genai.configure(api_key=api_key)

    # The system instruction defines the persona and constraints of the agent.
    system_instruction = (
        "You are a human problem diagnosis AI agent. "
        "Your only job is to identify the user's REAL problem, "
        "not to motivate, not to suggest solutions."
    )

    try:
        # Initialize the model with the system instruction
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=system_instruction
        )
        chat = model.start_chat(history=[])
    except Exception as e:
        print(f"Error initializing model: {e}")
        sys.exit(1)

    print("--- Human Problem Diagnosis Agent ---")
    print("Describe your situation, and I will help identify the core problem.")
    print("Type 'exit' or 'quit' to end the session.")
    print("-------------------------------------")

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting...")
                break

            if not user_input.strip():
                continue

            response = chat.send_message(user_input)
            print(f"Agent: {response.text}")

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            break

if __name__ == "__main__":
    main()
