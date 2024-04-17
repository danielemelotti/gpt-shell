import openai
import argparse #allows to pass arguments on command line
import os
from dotenv import load_dotenv

load_dotenv() #loading environment variables - your OpenAI API key

SYSTEM_MESSAGE = """
Answer the user with code snippets representing the ideal solution only.
Do not type in any other words.
"""

def main():
    print("Starting on GPT Shell Client")
    parser = argparse.ArgumentParser() #creating a parser

    # Adding arguments -- can be multiple words, with or without quotes around the prompt
    parser.add_argument(
        "prompt", nargs = "+", type = str, help = "Prompt for GPT-4 to complete"
    )
    
    args = parser.parse_args() #parse the arguments
    prompt = " ".join(args.prompt) #join the arguments into prompt

    # Print original prompt
    print(f"Q: {prompt}")

    chat_history = []

    # Calling the function to connect to GPT
    response = ask_gpt(prompt, chat_history, SYSTEM_MESSAGE)

    # Creating a loop so the chat does not end after the first prompt
    user_input = input("You: ")
    while user_input != "": #app will exit if you only press enter
        prompt = user_input
        ask_gpt(prompt, chat_history, SYSTEM_MESSAGE)
        user_input = input("You: ")

    print("Ending Session Now 👋")

# Function for sending code to ChatGPT
def ask_gpt(prompt: str, chat_history: list, system_message: str):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    client = openai.OpenAI() #initializing the openAI client

    try:
        user_prompt = {"role": "user", "content": prompt}

        response = client.chat.completions.create(
            model = "gpt-4",
            messages = [
                {"role": "system", "content": system_message},
                *chat_history, #let the GPT remember the conversation
                user_prompt, #latest prompt
            ]
        )
        content = response.choices[0].message.content #extracting GPT's reply
        chat_history.append(user_prompt) #append latest prompt to chat history
        chat_history.append({"role": "assistant", "content": content}) #append latest GPT's answer to chat history
        

        # Print text in green color
        print("\n\033[92m" + content + "\033[0m")
        return content
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error processing your request."

if __name__ == "__main__": #run the program when executed
    main()