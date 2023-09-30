from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot. exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('VaVBC8RFKt1TQ0EliEshIeM8IJm7o8N1argNIxnPi9f7KwRytljjNn/JP91lPLJitnEeDjEV79/XvzfkeyCTWdrBKCIUqoIsnWRIHG+C6hcr5CqhSM37Lq+lHS1k2pR2XtZIL506oPUR2de/khbcTQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('66c88089e0d2ef1f3640e5adc28fd25c')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == '__main__':
    app.run()
