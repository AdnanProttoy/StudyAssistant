# helper_bot.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_answer(question: str) -> str:
    """
    This function send the user's question to the OpenAI API and give the answer in Englis or Bangla
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful study assistant who explains topics in simple English and Bangla."},
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=300
        )
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        return f"Error: {e}"
