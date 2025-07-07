from openai import OpenAI
from config import OPENROUTER_API_KEY

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def ask_gpt(message, history=None):
    if history is None:
        history = []

    messages = [
        {"role": "system", "content": "You are a helpful travel assistant. Only answer questions strictly related to travel. Politely refuse any unrelated topics."}
    ]
    messages += history
    messages.append({"role": "user", "content": message})

    try:
        response = client.chat.completions.create(
            model="mistralai/mixtral-8x7b-instruct",
            messages=messages,
            temperature=0.7,
            max_tokens=300
        )

        reply = response.choices[0].message.content.strip()
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": reply})

        return reply, history

    except Exception as e:
        return f"\u274c OpenRouter Error: {e}", history
