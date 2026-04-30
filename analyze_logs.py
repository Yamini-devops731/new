import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("log.txt", "r") as f:
    log_data = f.read()

prompt = f"""
You are a DevOps expert.

Analyze this Jenkins pipeline failure log:
{log_data}

Give:
1. Root cause
2. Fix suggestion
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

print("\n=== AI ANALYSIS ===\n")
print(response.choices[0].message.content)
