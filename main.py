import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from call_function import available_functions
from prompts import system_prompt



def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

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
        config=types.GenerateContentConfig(
             tools=[available_functions],system_instruction=system_prompt
             )
    )

    if verbose:
        print(f"User prompt: {user_input}")
        print(f"Prompt tokens: {generated_content.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {generated_content.usage_metadata.candidates_token_count}")
    #print(generated_content.text)
   
    

    if generated_content.function_calls:
        function_call_part = generated_content.function_calls[0]
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
         print(generated_content.text)


if __name__ == "__main__":
    main()
