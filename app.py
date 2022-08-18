# from crypt import methods
from email import message
from unittest import result
from flask import Flask, render_template, url_for, request, jsonify
import requests
import json

# app = Flask(__name__)

sender = input("Name: ")
bot_message=""
# @app.route('/', methods = ['POST', 'GET'])
# def hello_world():
    
#     
#     return render_template('front.html', val = val)
while bot_message != "Bye":
    message=input("Message: ")
    print("Sending message")

    r = requests.post("http://localhost:5005/webhooks/rest/webhook", json={"Sender": sender, "message": message})

    print("Bot says, ", end = ' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{i['text']}")









# def Result():
#     if request.method=="POST":
#         print(list(request.form.values()))
#         result =list(request.form.values())[0]
#         if result.lower()=="restart":
#             output.clear()
#         else:
#             try:
#                 r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": sender, "message": message})
#                 print("Bot says, ")
#                 for i in r.json():
#                     bot_message = i['text']
#                     print(f"{i['text']}")
#                 output.extend([("message parker", result), ("message stark", "we are unable to pr")])
#             except:
#                 output.extend([("message parker", result),("message stark", "we are unable to process your request")])

#         print(output)
#         return render_template("")

# if __name__ == "__main__":
#     app.run(debug = True, port = 5000)