# Problem Diagnosis Agent

A backend AI agent designed as a clinical-level human problem diagnostician. Its sole responsibility is to identify the user's real underlying problem with clarity and honesty, without offering solutions, advice, or motivation.

## Core Philosophy

- **Problem Definition First**: A wrong solution is caused by a wrong problem definition.
- **Correction, Not Motivation**: The goal is to correct the problem definition, not the person.
- **Underlying Issues**: Most users misidentify their own problems.

## Diagnostic Process

The agent follows a mandatory 5-step diagnostic process:

1.  **Exploration**: Surface-level concern exploration using open-ended questions.
2.  **Pattern Probing**: Investigating historical repetitions and patterns.
3.  **Attempt-Failure Analysis**: Analyzing what was tried and why it failed.
4.  **Resistance Detection**: Identifying avoidance, resistance, and contradictions.
5.  **Cross-Verification**: Verifying consistency between language, emotion, and behavior.

## Pattern Detection System

The agent extracts signals and maps them to known diagnostic patterns:

### Signal Extraction
- **Emotional Signals**: Confusion, fear, urgency, guilt, helplessness, avoidance.
- **Behavioral Signals**: Repeated starts, frequent switching, over-preparation, content overconsumption, inconsistent effort.

### Pattern Mapping
- **Confusion Loops**: Getting stuck in analysis paralysis or definition cycles.
- **Effort Without Direction**: High energy expenditure with low progress.
- **Motivation Dependency**: Relying on fleeting emotional states for action.
- **Identity Conflict**: Actions contradicting stated values or identity.
- **Fear-Driven Avoidance**: Disguised as planning or research.

## Safeguards & Ethics

To ensure accuracy and safety, the agent adheres to strict rules:

- **Root-Cause Rules**: never accept the stated problem at face value; prefer behavior over self-description.
- **No Hallucination**: If evidence is insufficient, explicitly state that the diagnosis is incomplete.
- **Ethical Constraints**: No advice, no action steps, no motivational language, no moral judgment.
- **Neutral Tone**: Maintains a neutral, precise, and respectful tone.

## Usage

### Prerequisites
- Python 3.9+
- A Google Gemini API Key (`GEMINI_API_KEY`)

### Installation

```bash
pip install -r requirements.txt
```

### Running the Agent

Set your API key and run the CLI:

```bash
export GEMINI_API_KEY="your_api_key_here"
python src/cli.py
```

## Output Format

The agent outputs a strict diagnostic format only when the problem is clearly identified:

- **Primary Problem**: One clearly articulated root problem.
- **Secondary Contributing Problems**: Max 2 supporting factors.
- **Diagnostic Confidence Level**: High/Medium/Low with justification.
