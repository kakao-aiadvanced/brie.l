from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

system_content_list = [
'''
주어진 리스트에서 1부터 n까지의 자연수 중 m개의 숫자가 있습니다. 이 리스트를 오름차순으로 정렬하세요. 답변에는 정렬된 리스트만 포함해주세요.

예시:

입력: [10, 3, 7, 2, 5]
출력: [2, 3, 5, 7, 10]
''',
'''
아래 주어진 리스트는 1부터 n까지의 자연수 중 m개의 숫자입니다. 이 리스트를 오름차순으로 정렬하고, 정렬된 리스트만 답변하세요.

예시:

입력: [6,3,9,4]
출력: [3, 4, 6, 9]
''',
'''
1부터 n까지의 자연수 중 m개의 숫자가 포함된 리스트를 정렬하세요. 오름차순으로 정렬된 리스트를 답변으로 제출해주세요. 답변에는 리스트 외에 자연어를 포함하지 마세요.
''',
]

content_test = [
  '[10, 5, 3, 8, 1]',
  '[6, 1, 5]',
  '[18, 11, 5, 2, 15, 7]',
  '[13,6,11,444,8]',
  '[191909, 12, 3, 14, 7]',
]

def get_answer(system_content, user_content):
  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": system_content},
      {"role": "user", "content": user_content},
    ]
  )
  return completion.choices[0].message.content

for ver, system_content in enumerate(system_content_list):
  print(f'--------------- prompt {ver+1} ----------------')
  print(system_content)
  point = 0
  for content in content_test:
    print(f'>>> input: {content}')
    answer = get_answer(system_content, content)
    print(f'output: {answer}')
    try:
      answer = eval(answer)
    except:
      print('Failed')
    else:
      if answer == sorted(answer):
        print('Success')
        point += 1
      else:
        print('Failed')
  print(f'Success Rate: {point * 100 / 5}%')


