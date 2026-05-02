# Steam Price Parser

Веб-приложение на Flask для парсинга цен игр из Steam по URL и сохранения в JSON.

## Возможности

- Парсинг актуальных цен игр Steam по ссылке
- Сохранение данных в JSON-файл
- Простой веб-интерфейс

## Технологии

- Python 3.x
- Flask
- BeautifulSoup4 / requests (для парсинга)
- JSON

## Установка и запуск
Создать виртуальное окружение:

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows


Установить зависимости:
pip install flask requests beautifulsoup4

Запустить приложение:
python app.py


Открыть в браузере:
http://localhost:5000

Клонировать репозиторий:
```bash
git clone https://github.com/ваш_логин/steam-price-parser.git
cd steam-price-parser



