import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
parser = argparse.ArgumentParser(description="A description of your script.")
parser.add_argument("prompt", help="The prompt to pass to the LLM.")
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output.")

args = parser.parse_args()

if __name__ == "__main__":
    if len(args.prompt) > 1:
        user_prompt = sys.argv[1]
        messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
        response = client.models.generate_content(
            model = "gemini-2.0-flash-001",
            contents = messages)
        print(response.text)
        
        if args.verbose:
            print(f"User prompt: {messages}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print("error receiving argument")
        sys.exit(1)