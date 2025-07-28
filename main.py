import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import available_functions, call_function
from prompts import system_prompt
from config import MAX_ITERATIONS



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
     
     iterations = 0
     while True:
          iterations += 1
          if iterations > MAX_ITERATIONS:
               print(f"Maximum iterations ({MAX_ITERATIONS}) reached.")
               sys.exit(1)

          try:
               final_response = generate_content(client, messages, verbose)
               if final_response:
                    print("Final response:")
                    print(final_response)
                    break
          except Exception as e:
               print(f"Error while generating content: {e}")


def generate_content(client, messages, verbose):
     generated_content = client.models.generate_content(
          model="gemini-2.0-flash-001",
          contents=messages,
          config=types.GenerateContentConfig(
               tools=[available_functions],system_instruction=system_prompt
          )
     )

     if generated_content.candidates:
          for candidate in generated_content.candidates:
               function_call_content = candidate.content
               messages.append(function_call_content)

     if verbose:
          print(f"Prompt tokens: {generated_content.usage_metadata.prompt_token_count}")
          print(f"Response tokens: {generated_content.usage_metadata.candidates_token_count}")

     if not generated_content.function_calls:
          return generated_content.text
     

     function_responses = []
     for function_call_part in generated_content.function_calls:
          function_call_result = call_function(function_call_part, verbose)
          if not function_call_result.parts or not function_call_result.parts[0].function_response:
               raise Exception("Fatal: Empty function call result")

          if verbose:
               print(f"-> {function_call_result.parts[0].function_response.response}")

          function_responses.append(function_call_result.parts[0])

     if not function_responses:
          raise Exception("no response generated, exiting.")

if __name__ == "__main__":
    main()
