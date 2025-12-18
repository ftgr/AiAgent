import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("API key was not found")

client = genai.Client(api_key=api_key)


def main():
    parser = argparse.ArgumentParser(description="AI Agent Chatbot written in Python")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    #parser.add_argument("--verbose", type=bool, )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`

    #user_prompt = args.user_prompt

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(
    model='gemini-2.5-flash', contents=messages)

    if response is None:
        raise RuntimeError("usage_metadata is None")
    else:
        usage = response.usage_metadata
        if not args.verbose:
            print(f"Response: {response.text}")
        else:
            print(f"User prompt: {messages}\nPrompt tokens: {usage.prompt_token_count}\nResponse tokens: {usage.candidates_token_count}\nResponse:\n{response.text}")
        

if __name__ == "__main__":
    main()
