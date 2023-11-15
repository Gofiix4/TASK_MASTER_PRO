import openai

openai.api_key = "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"
pregunta = openai.Completion.create(engine="text-davinci-003",
                                    prompt="¿Que es chatgpt?",
                                    max_tokens=2048)

print(pregunta.choices[0].text)