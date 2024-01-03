from suds.client import Client

url = 'http://localhost:8000/?wsdl'
client = Client(url)


def question():

    while True:
        quest = input("Ta question: ")
        request  = client.service.ask_ai(quest)

        print(request)

def chat():
    quest = input("Vous: ")
    requests = client.service.chat_ai(quest)
    print(requests)


question()