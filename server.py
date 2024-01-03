from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import google.generativeai as genai
from sql import create_database

genai.configure(api_key="GOOGLE-API-KEY")


class HelloWorldService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def say_hello(ctx, name):
        return "Hello, %s!" % name




    @rpc(Unicode, _returns=Unicode)
    def ask_ai(ctx, ask):
        genai.configure(api_key="AIzaSyCjdaJ4x7iYR7Sbgi76oLN71qk8DX02pzU")
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(ask)

        resp = str(response)
        questions = []
        for i in questions:
            questions.append(response)
            print(questions)

        return str(response.text)

    #@rpc(Unicode, _returns=Unicode)
    #def chat_ai(ctx,ask):
     #   model = genai.GenerativeModel('gemini-pro')
      #  chat  = model.start_chat()
       # while True:
        #    message = input("Vous: " )
         #   response = chat.send_message(message)

          #  return print("Gemini: " + response.text)





application = Application([HelloWorldService], tns='http://example.com/hello', in_protocol=Soap11(), out_protocol=Soap11())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(application)
    server = make_server('localhost', 8000, wsgi_app)
    server.serve_forever()
