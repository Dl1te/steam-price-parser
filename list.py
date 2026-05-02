from get_price import get_price
import json
from pathlib import Path


games = []
DATA_FILE = "data.json"


def list_append(url):
    try:
        name, price, url = get_price(url)
        game_name = name
        game_price = price

        # 1. Загружаем существующие данные (всегда как список)
        games = []
        if Path(DATA_FILE).exists():
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                try:
                    games = json.load(file)
                    if not isinstance(games, list): # Страховка: если в файле не список
                        games = []
                except json.JSONDecodeError:
                    games = []
        # 2. Добавляем новый словарь в список
        games.append({
            "name": game_name,
            "price": game_price,
            "url": url
        })
        if name in games:
            pass
        # 3. Сохраняем обратно
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(games, file, ensure_ascii=False, indent=4)
        print(f"Игра '{game_name}' добавлена!")

    except Exception as e:
        print(f"Ошибка при добавлении: {e}")


def list_dell(del_game):
    if Path(DATA_FILE).exists():
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            games = json.load(file)
        new_games = [g for g in games if g.get("name") != del_game]
        if len(new_games) < len(games):
            with open(DATA_FILE, "w", encoding="utf-8") as file:
                json.dump(new_games, file, ensure_ascii=False, indent=4)
            print(f"Игра '{del_game}' удалена.")
        else:
            print("Такой игры нет в списке.")
    else:
        print("Файл данных не найден.")


