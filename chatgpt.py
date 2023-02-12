import os
import openai

openai.apikey = os.environ.get('OPENAI_KEY')

while True:
    prompt = input("\n Introduce el prompt a chatgpt-3 o 'exit' para salir")

    if prompt == "exit":
        break

    completation = openai.Completation.create(engine="text-davinci-003",
                            prompt=prompt,
                            n=1,
                            max_tokens="2048")

    print(completation.choices[0].text)