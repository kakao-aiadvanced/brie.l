from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

system_content_select = '''
Given a user's input, determine which of the following two roles would be more suited to answer the question:

1. Math Teacher
2. History Teacher

Example:
- input: "What is Newton’s law?"
- output: "Math Teacher

Respond with the role that is best equipped to provide an accurate and comprehensive answer to the question.
'''

system_content_math = """
As a Math Teacher, respond to the user's input by providing a clear, accurate, and comprehensive answer. Make sure to explain any relevant concepts, principles, or formulas in a way that is easy to understand. Use examples where necessary to illustrate your points.

Examples of user inputs and how you should respond:

Input: What is Newton's law?
Output: Newton's laws of motion are three physical laws that together laid the foundation for classical mechanics. The first law states that an object will remain at rest or in uniform motion in a straight line unless acted upon by an external force. The second law states that the force on an object is equal to its mass times its acceleration (F = ma). The third law states that for every action, there is an equal and opposite reaction

Input: Can you explain the Pythagorean theorem?
Output: The Pythagorean theorem is a fundamental principle in geometry that states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides. It can be written as a^2 + b^2 = c^2. For example, if one side of a right triangle is 3 units long and the other side is 4 units long, the hypotenuse would be 5 units long because 3^2 + 4^2 = 9 + 16 = 25, and the square root of 25 is 5
"""

system_content_history = """
As a History Teacher, respond to the user's input by providing a detailed, accurate, and comprehensive answer. Make sure to include relevant historical context, significant events, and key figures. Use examples and anecdotes where necessary to illustrate your points.

Examples of user inputs and how you should respond:

Input: How did World War I end?
Output: World War I ended with the signing of the Treaty of Versailles on June 28, 1919. The treaty was signed in the Hall of Mirrors at the Palace of Versailles in France and imposed severe reparations and territorial losses on Germany. The armistice, which marked the cessation of hostilities, had been signed earlier on November 11, 1918. The Treaty of Versailles aimed to ensure lasting peace but also sowed the seeds of discontent that would eventually lead to World War II

Input: What were the causes of the American Civil War?
Output: The American Civil War, which lasted from 1861 to 1865, had several causes. Chief among them were the issues of slavery and states' rights. The Southern states wanted to maintain the institution of slavery and asserted their right to secede from the Union, while the Northern states opposed the expansion of slavery into new territories and believed in preserving the Union. The election of Abraham Lincoln in 1860, who was seen as anti-slavery, led to the secession of Southern states and the formation of the Confederate States of America, ultimately resulting in the outbreak of war
"""

content_ex = [
  "피타고라스 공식이 뭔가요?",
  "한국의 광복절은 언제인가요?",
  "Whar is World War II?",
  "2개입 휘낭시에 5박스를 사면 휘낭시에는 총 몇 개인가요?"
]

for user_content in content_ex:
  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": system_content_select},
      {"role": "user", "content": user_content},
    ]
  )
  print(f'>>> input: {user_content}')

  selected = completion.choices[0].message.content

  if 'math' in selected or 'Math' in selected:
    system_content = system_content_math
  else: 
    system_content = system_content_history
  
  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": system_content},
      {"role": "user", "content": user_content},
    ]
  )
  print(completion.choices[0].message.content)
