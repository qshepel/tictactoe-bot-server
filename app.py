from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7794390382:AAEtr0y3a-PArzp5bKTjm4eJqQFfneMDWeo"
WEB_APP_URL = "https://tictactoe-miniapp.vercel.app"  # временный адрес

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if "message" in data and "text" in data["message"]:
        chat_id = data["message"]["chat"]["id"]
        if data["message"]["text"].lower() == "/start":
            send_webapp_button(chat_id)
    return "ok"

def send_webapp_button(chat_id):
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={
        "chat_id": chat_id,
        "text": "Запусти игру:",
        "reply_markup": {
            "inline_keyboard": [[{
                "text": "▶️ Играть",
                "web_app": {"url": WEB_APP_URL}
            }]]
        }
    })

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)

