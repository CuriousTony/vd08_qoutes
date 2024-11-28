from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


def get_random_quote():
    response = requests.get('https://api.quotable.io/random', verify=False)
    if response.status_code == 200:
        return response.json()
    return {"content": "Ошибка при получении цитаты", "author": "Неизвестно"}


@app.route('/')
def index():
    quote = get_random_quote()
    return render_template('index.html', quote=quote)


@app.route('/next-quote', methods=['GET'])
def next_quote():
    quote = get_random_quote()
    return jsonify(quote)


if __name__ == '__main__':
    app.run(debug=True)