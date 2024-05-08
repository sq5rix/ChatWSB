import os
import openai
from dotenv import load_dotenv
from czyt_pdf import read_all_files
from prompts import general_prompt, GPT_MODEL

def infer_chat(prompt):
    """
    Generates text based on the given prompt using OpenAI's GPT-4 API.

    Args:
    prompt (str): The prompt to generate text from.
    api_key (str): Your API key for OpenAI.

    Returns:
    str: The generated text.
    """

    load_dotenv()

    api_key = os.getenv("OPENAI_KEY")
    openai.api_key = api_key

    response = openai.chat.completions.create(
        model=GPT_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )
    return response.choices[0].message.content

def main():
    infer_chat = generate_text(f"Treść: {read_all_files()} Pytanie: {general_prompt}")
    print(generated_text )

if __name__ == "__main__":
    main()

