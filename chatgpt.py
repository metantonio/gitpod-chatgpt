import os
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')

while True:
    prompt = input("\n Introduce el prompt a chatgpt-3 o 'exit' para salir\n")

    if prompt == "exit":
        break

    completation = openai.Completion.create(engine="text-davinci-003",
                            prompt=prompt,
                            n=1,
                            max_tokens=4096)

    print(completation.choices[0].text)