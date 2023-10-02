#LINEBOT SERVER PROGRAM
from flask import Flask 
app = Flask(__name__)

#import modules nessary for LINEBOT
from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot. exceptions import InvalidSignatureError 
from linebot.models import MessageEvent, TextMessage, TextSendMessage

#channel secret:assess token: checking returning message
line_bot_api = LineBotApi('VaVBC8RFKt1TQ0EliEshIeM8IJm7o8N1argNIxnPi9f7KwRytljjNn/JP91lPLJitnEeDjEV79/XvzfkeyCTWdrBKCIUqoIsnWRIHG+C6hcr5CqhSM37Lq+lHS1k2pR2XtZIL506oPUR2de/khbcTQdB04t89/1O/w1cDnyilFU=')
#checking the eligibility of inputs message
handler = WebhookHandler('66c88089e0d2ef1f3640e5adc28fd25c')


#checking if correctly receive input message
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature'] 
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

#generating output message
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text)) #replying users' inputs

if __name__ == '__main__':
    app.run()
