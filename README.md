# gpt-shell

gpt-shell is a command-line interface tool designed to interact with OpenAI's GPT-4 model to generate code snippets based on prompts provided by the user. This tool leverages the powerful language model to assist developers by providing coding solutions directly from the command line.

## Features

- **Interactive Chat**: Continuously interact with GPT-4 to refine code solutions based on a sequence of user inputs.
- **Code Snippet Generation**: Receives user prompts and returns precise code snippets **without** additional commentary.
- **Session Memory**: Maintains a history of the chat within a session to provide contextually relevant responses.

## Prerequisites

Before you start using gpt-shell, you need to set up a few things:

- Python 3.6 or higher.
- An OpenAI API key. You can obtain one by creating an account at [OpenAI](https://openai.com/).

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/gpt-shell.git
   cd gpt-shell
   ```

2. **Install dependencies**:
This project requires openai Python library. Install it using pip:
`pip install openai`

3. **Set up the environment variable:**
Create a .env file in the project directory and add your OpenAI API key:
`OPENAI_API_KEY=your_openai_api_key_here`

Replace your_openai_api_key_here with your actual OpenAI API key.

## Usage
To start a session with gpt-shell, run the following command in your terminal:
`python gpt.py "Your initial prompt here"`

Keep the session going by providing further inputs. To end the session, simply press Enter without typing anything.

## Example
Here's how you can use gpt-shell:
`python gpt.py "Create a Python function to reverse a string"`

Follow the instructions on the screen to continue the interaction or to end it.
