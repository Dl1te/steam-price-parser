import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import json
from pathlib import Path
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def get_price(url: str) -> tuple[str, str, str]:
    ua = UserAgent()
    header = {"User-Agent": ua.random,
             'Accept-Language': 'ru-US,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7,en;q=0.6' 
             }
    res = requests.get(url, headers=header, timeout=10).text
    soup = BeautifulSoup(res, 'lxml')
    
    # Название из title
    name = soup.find('title').get_text().split('в Steam')[0].strip()
    
    # Цена с обработкой ошибок
    price_elem = soup.find(class_="game_purchase_price price")
    if not price_elem:
        price_elem = soup.find(class_="discount_final_price")
    price = price_elem.get_text().strip() if price_elem else "Цена не указана"
    return name, price, url



def update_prices():
    path = Path("data.json")
    if not path.exists():
        print("Файл data.json не найден")
        return
    with open(path, "r", encoding="utf-8") as file:
        try:
            games = json.load(file)
        except json.JSONDecodeError:
            return
    # Проходим по каждой игре и обновляем цену
    for item in games:
        print(f"Обновляю {item.get('name')}...")
        result = get_price(item['url'])
        if result:
            new_name, new_price, _ = result
            item['price'] = new_price # Прямо обновляем значение в словаре
            item['name'] = new_name   # На всякий случай обновляем имя
    # Сохраняем обновленный список обратно в файл
    with open(path, "w", encoding="utf-8") as file:
        json.dump(games, file, ensure_ascii=False, indent=4)
    print("Все цены обновлены!")

