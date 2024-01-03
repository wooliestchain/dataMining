import pprint
import google.generativeai as palm

palm.configure(api_key='AIzaSyCjdaJ4x7iYR7Sbgi76oLN71qk8DX02pzU')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)

prompt = input("Entrer une phrase: ")

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)
print(completion.result)