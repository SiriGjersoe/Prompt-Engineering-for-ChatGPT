"""
Author: Siri Moen Gjersøe
Description:
Interactive Python script that helps you create an In-Persona prompt.
It asks a few short questions and combines your answers into a complete,
ready-to-copy prompt for ChatGPT or any large language model.
"""

def build_prompt():
    print("In-Persona Prompt Builder")
    print("-----------------------------")

    # Ask user for each part of the prompt
    persona = input("👤 Who or what is the persona (e.g., 'experienced linguist', 'UX designer')? ").strip()
    expertise = input("🎓 What is their expertise or defining trait? ").strip()
    goal = input("What is their main goal or task? ").strip()
    tone = input("What tone or communication style should they use (e.g., academic, friendly, concise)? ").strip()
    audience = input("👥 Who is the target audience (e.g., students, business professionals)? ").strip()
    constraints = input(" Any constraints or special rules (e.g., use Norwegian, avoid technical jargon)? ").strip()

    # Build formatted prompt
    full_prompt = f"""
You are a {persona}, known for {expertise}.
Your goal is to {goal}.
You communicate in a {tone} manner.
Your target audience is {audience}.
{f"Constraints: {constraints}" if constraints else ""}

Now, perform the task accordingly.
"""

    # Show the result
    print("\n Here’s your full In-Persona prompt:\n")
    print(full_prompt)
    print("--------------------------------------------------")
    print("💡 Tip: Copy this prompt into ChatGPT or any LLM tool.")

if __name__ == "__main__":
    build_prompt()
