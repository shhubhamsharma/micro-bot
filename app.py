from flask import Flask,request
import random
from textblob import TextBlob

from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'EAAbt8KW5n7MBALL8e58ZAFlv21yfE0jInFL5ZBRCO3ATb0RmBbKQzGZCIYxWvJT660zIunCd3dZCZB0uWVb0k463KQ334bzZB1JqsQIqwSrZBwnQD11OQHJT2v6j75jci3dPZB430o5MwcNVVZCZBy1v0JSxZByNrlagns4iHuADATmLzZCtC8QhEUxO'
VERIFY_TOKEN = 'EAAbt8KW5n7MBALL8e58ZAFlv21yfE0jInFL5ZBRCO3ATb0RmBbKQzGZCIYxWvJT660zIunCd3dZCZB0uWVb0k463KQ334bzZB1JqsQIqwSrZBwnQD11OQHJT2v6j75jci3dPZB430o5MwcNVVZCZBy1v0JSxZByNrlagns4iHuADATmLzZCtC8QhEUxO'
bot = Bot(ACCESS_TOKEN)
Greeting_Keywords=("hello", "hi", "greetings", "sup", "what's up",'hey',)
Greeting_Response=['hey how may i help you?','hey','hi']


@app.route('/', methods=['GET', 'POST'])
def receive_message():
    output = request.json
    print(output)
    if request.method == 'GET':
        if request.args.get("hub.verify_token")==ACCESS_TOKEN :
            return request.args.get("hub.challenge")
    else:
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):  #text message
                        message_text= message['message'].get('text')
                        if message_text.lower() in Greeting_Keywords:
                            response_sent_text =random.choice(Greeting_Response)
                            bot.send_text_message(recipient_id, response_sent_text)
                        else:
                            response_sent_text ="Thank You for contacting we will connect with you soon"
                            bot.send_text_message(recipient_id, response_sent_text)
                        
                    if message['message'].get('attachments'):           #non text message
                        response_sent_nontext = "I don't know what does this mean?"
                        bot.send_text_message(recipient_id, response_sent_nontext)
    return "Message is Sent"
 
 
if __name__ == '__main__':
    app.run(debug=True)