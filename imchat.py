import os
import openai
from dotenv import load_dotenv
from czyt_pdf import read_all_files



GPT_4 = 'gpt-4-0613'
GPT_T = 'gpt-3.5-turbo'
GPT_MODEL = GPT_4

def generate_text(text, prompt):
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
                "content": f"Treść: {text} Pytanie: {prompt}",
            }
        ],
    )
    return response.choices[0].message.content

def main():
    prompt = """

    Treść uprzednio podłączona do promptu składa się z ciągu odpowiedzi na pytania.
    Treśc ma następujące pola w każdej z kolejnych odpowiedzi:
        Imię, potem imię,
        Nazwisko, potem właściwe nazwisko,
        a później pytanie i po nim treśc pytania, treść odpowiedzi.
        Jakie jest Imię i Nazwisko osoby, która napisała o brokerach?

    """
    generated_text = generate_text(read_all_files(), prompt)
    print(generated_text )

if __name__ == "__main__":
    main()

