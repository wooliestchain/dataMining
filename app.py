from flask import Flask, render_template, request
import google.generativeai as genai

genai.configure(api_key="AIzaSyCjdaJ4x7iYR7Sbgi76oLN71qk8DX02pzU")

app = Flask(__name__)

def chat_with():
    model = genai.GenerativeModel('gemini-pro')

    chat  = model.start_chat()

    while True:
        message = input("Vous: ")
        response = chat.send_message(message)

        print("Gemini: " + response.text)
        #print(chat.history)


@app.route('/')
def home():


    return render_template('index_chat.html')



@app.route('/submit')
def submit():
    message = request.args.get('message')
    #model = genai.GenerativeModel('gemini-pro')
    #response = model.generate_content(message)
    #resp = response.text
    return render_template('index_chat.html')


@app.route('/bot')
def bot():
    return render_template('bot.html')

if __name__ == '__main__':
    app.run(debug=True)
