from openai import OpenAI
# OpenAI library internally looks for OPENAI_API_KEY when client = OpenAI()
client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Say hello world"
        }
    ]
)
print(completion.choices[0].message.content)
