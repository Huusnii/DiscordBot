from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Beep Boop I am still alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()