from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

system_content = '''
Given a user's input, determine which of the following two roles would be more suited to answer the question:

1. Math Teacher
2. History Teacher

Example:
- input: "What is Newton’s law?"
- output: "Math Teacher

Respond with the role that is best equipped to provide an accurate and comprehensive answer to the question.
'''

content_ex = [
  "피타고라스 공식이 뭔가요?",
  "한국의 광복절은 언제인가요?",
  "Whar is World War II?",
  "Can you explain the Pythagorean theorem",
]

for user_content in content_ex:
  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": system_content},
      {"role": "user", "content": user_content},
    ]
  )
  print(f'input: {user_content}')
  print(completion.choices[0].message)
