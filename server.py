from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

RASA_SERVER_URL = 'http://localhost:5005/webhooks/rest/webhook'
TELEGRAM_API_URL = 'https://api.telegram.org/bot7181021887:AAGOJYh1LnnYuIqUyHLHYUxRPk1ruEx4Eow/sendMessage'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data['message']
    chat_id = message['chat']['id']
    text = message['text']

    # Check if language selection message
    if text.lower() in ['english', 'russian']:
        if text.lower() == 'english':
            language = 'en'
        else:
            language = 'ru'
        response_text = f'You have chosen {text.capitalize()}.'

        requests.post(TELEGRAM_API_URL, json={
            'chat_id': chat_id,
            'text': response_text
        })

        # Save language preference for future messages
        # You might want to store this in a database or a session

    else:
        # Send the message to Rasa with language metadata
        response = requests.post(RASA_SERVER_URL, json={
            'sender': chat_id,
            'message': text,
            'metadata': {'language': language}
        })

        for res in response.json():
            requests.post(TELEGRAM_API_URL, json={
                'chat_id': chat_id,
                'text': res['text']
            })

    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(port=5000)
