
from openai import OpenAI
api_key = "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"

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

try:
    response = client.chat.completions.create(
        model="mistralai/mixtral-8x7b-instruct"
,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
        ],
        temperature=0.7,
        max_tokens=100
    )

    
    print("✅ SUCCESS:", response.choices[0].message.content.strip())

except Exception as e:
    print("❌ ERROR:", e)
