import google.generativeai as genai

genai.configure(api_key="AIzaSyCjdaJ4x7iYR7Sbgi76oLN71qk8DX02pzU")

#for m in genai.list_models():
 #   if "generateContent" in m.supported_generation_methods:
  #      print(m.name)


#model = genai.GenerativeModel('gemini-pro')

#response  = model.generate_content("Beyond the shadow you settle for there is a miracle illuminated")

#print(response.text)

import PIL.Image

img = PIL.Image.open('téléchargement.jpeg')
model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(["Describe this image", img])
print(response.text)
