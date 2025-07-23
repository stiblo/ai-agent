import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types





def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'

    verbose = False
    if "--verbose" in sys.argv:
         verbose = True

    script_args = sys.argv[1:]
    filtered_args = []

    for arg in script_args:
         if not arg.startswith("--"):
              filtered_args.append(arg)

    if not filtered_args:
            print(f"ERROR: No user prompt provied!")
            print(f'\nUsage: python main.py "YOUR PROMPT HERE" [--verbose]')
            sys.exit(1)
    user_input = " ".join(filtered_args)

    messages = [
         types.Content(role="user", parts=[types.Part(text=user_input)]),
    ]

    generated_content = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt)
    )

    if verbose:
        print(f"User prompt: {user_input}")
        print(f"Prompt tokens: {generated_content.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {generated_content.usage_metadata.candidates_token_count}")
    print(generated_content.text)

if __name__ == "__main__":
    main()
