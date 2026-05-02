from flask import Flask, render_template, request
from get_price import get_price
from get_price import update_prices
from list import list_append
from list import list_dell
import json
import socket


app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')


def get_local_ip():
    try:
        # Создаем сокет для определения IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


@app.route('/run-function', methods=['POST', 'GET'])
def reload_price():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data_list = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data_list = []
    games = []
    price_data = None
    if request.method == "POST":
        url = request.form.get('url')
        if url:
            
            price_data = (url) 
            games = list_append(url)
    return render_template("index.html", price=price_data, game_name=games, items=data_list)


@app.route('/', methods=["GET", "POST"])
def index():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data_list = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data_list = []
    games = []
    price_data = None
    if request.method == "POST":
        url = request.form.get('url')
        if url:
            
            price_data = get_price(url) 
            games = list_append(url)
    return render_template("index.html", price=price_data, game_name=games, items=data_list)


@app.route('/d', methods=["GET", "POST"])
def del_game_route():
     # Переименовали функцию роута, чтобы не путаться
    target_game = None # Переменная для шаблона (что именно удалили)
    
    if request.method == "POST":
        game_to_del = request.form.get('name') # Получаем имя из формы
        if game_to_del:
            list_dell(game_to_del) # Вызываем вашу функцию удаления с аргументом
            target_game = game_to_del # Запоминаем имя для вывода в шаблоне
            
    # Загружаем список заново, чтобы в del.html был актуальный список без удаленной игры
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data_list = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data_list = []
        
    return render_template("del.html", items=data_list, name_game=target_game)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
    local_ip = get_local_ip()
    print(f"   → http://{local_ip}:5000")