import os
from dotenv import load_dotenv  
from openai import OpenAI
load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("OPENAI_API_KEY")  # Get the API key from environment variables
if not api_key:
    raise ValueError("OPENAI_API_KEY was not found. Check your .env file.")  # Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)  # Create the OpenAI client
print("V.A.N.T.A. is online.")
print("Type 'exit' to shut me down.")
conversation_history = []  # Initialize an empty list to store conversation history
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("V.A.N.T.A. is shutting down. Goodbye!")
        break
    else:
        conversation_history.append({"role": "user", "content": user_input})
        response = client.responses.create(
            model="gpt-5",
            instructions="You are V.A.N.T.A., Jeremy's personal AI assistant. Your name is V.A.N.T.A. Be intelligent, concise, practical, and helpful. When asked who you are, identify yourself as V.A.N.T.A.",
            input=conversation_history
        )
        conversation_history.append({"role": "assistant", "content": response.output_text}) 
        print(f"V.A.N.T.A.: {response.output_text}")