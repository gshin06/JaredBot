import openai

openai.api_key = "Hidden"

promptInput = input('What would you like to ask me?\n')


response = openai.Completion.create(
  model="Hidden",
  prompt= promptInput,
  temperature=0.7,
  max_tokens = 25,
  stop = ['.', '?', '!', '\n<return>'],
  top_p = 1,
  frequency_penalty = 1
)

print(response['choices'][0]['text'])