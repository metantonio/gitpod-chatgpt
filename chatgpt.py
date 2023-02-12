import os
import openai

openai.apikey = os.environ.get('OPENAI_KEY')

completation = openai.Completation.create(engine="text-davinci-003",
                           prompt="Qué es chatgpt?",
                           n=1,
                           max_tokens="2048")

print(completation.choices[0].text)