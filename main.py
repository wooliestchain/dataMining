import google.generativeai as genai
import os

genai.configure(api_key="GOOGLE-API-KEY")


def chat_with():
    model = genai.GenerativeModel('gemini-pro')

    chat  = model.start_chat()

    while True:
        message = input("Vous: ")
        response = chat.send_message(message)

        print("Gemini: " + response.text)

        ch = chat.history

        story = []

        story.append(ch)

        print(story)


def quiz():
    from train_final import model

    while True:
        ask = input("Vous: ")
        response = model.generate_content(ask)
        print(response.text)

quiz()


