import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import requests
import datetime
import time

def get_time_data():
    url = "https://yandex.com/time/sync.json?geo=213"
    
    try:
        # a) Запрос и вывод сырого ответа
        print("Отправка запроса к API...")
        start_request = time.perf_counter()  # Точный замер времени
        response = requests.get(url, timeout=5)  # Таймаут 5 секунд
        request_duration = time.perf_counter() - start_request
        
        print("\nСырой ответ от API:")
        print(response.text)
        
        data = response.json()
        
        # b) Человекочитаемое время и временная зона
        timestamp = data['time'] / 1000
        human_time = datetime.datetime.fromtimestamp(timestamp)
        
        # Получаем временную зону
        timezone = data.get('clocks', {}).get('213', {}).get('name', 'не указана')
        
        print(f"\nТекущее время: {human_time}")
        print(f"Временная зона: {timezone}")
        print(f"Время выполнения запроса: {request_duration:.3f} сек.")
        
        # c) Замер дельты времени
        print("\nЗамер задержки...")
        start_time = time.perf_counter()
        response = requests.get(url, timeout=5)
        data = response.json()
        server_time = datetime.datetime.fromtimestamp(data['time'] / 1000)
        delta = (time.perf_counter() - start_time) * 1000  # в миллисекундах
        
        print(f"Дельта времени (1 запрос): {delta:.3f} мс.")
        
        # d) Средняя дельта по 5 запросам
        print("\nИзмерение средней задержки (5 запросов)...")
        deltas = []
        for i in range(5):
            start = time.perf_counter()
            response = requests.get(url, timeout=5)
            data = response.json()
            delta = (time.perf_counter() - start) * 1000
            deltas.append(delta)
            print(f"Запрос {i+1}: дельта = {delta:.3f} мс.")
            time.sleep(1)  # Пауза между запросами
        
        avg_delta = sum(deltas) / len(deltas)
        print(f"\nСредняя дельта: {avg_delta:.3f} мс.")

    except Exception as e:
        print(f"\n⚠️ Ошибка: {e}")

if __name__ == "__main__":
    get_time_data()