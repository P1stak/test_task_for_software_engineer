import requests
import datetime
import time

def get_time_data():
    url = "https://yandex.com/time/sync.json?geo=213"
    
    # Запрос и вывод сырого ответа
    response = requests.get(url)
    print("Сырой ответ:")
    print(response.text)
    
    # Человекочитаемый формат и временная зона
    data = response.json()
    timestamp = data['time'] / 1000  # преобразуем в секунды
    human_time = datetime.datetime.fromtimestamp(timestamp)
    timezone = data['clocks'][0]['name']
    
    print(f"\nЧеловекочитаемое время: {human_time}")
    print(f"Временная зона: {timezone}")
    
    # Дельта времени
    start_time = datetime.datetime.now()
    response = requests.get(url)
    data = response.json()
    server_time = datetime.datetime.fromtimestamp(data['time'] / 1000)
    delta = server_time - start_time
    
    print(f"\nДельта времени (1 запрос): {delta.total_seconds()} секунд")
    
    # Средняя дельта по 5 запросам
    deltas = []
    for i in range(5):
        start = datetime.datetime.now()
        response = requests.get(url)
        data = response.json()
        server_time = datetime.datetime.fromtimestamp(data['time'] / 1000)
        delta = server_time - start
        deltas.append(delta.total_seconds())
        print(f"Запрос {i+1}: дельта = {delta.total_seconds()} секунд")
        time.sleep(1)  # чтобы не нагружать сервер
    
    avg_delta = sum(deltas) / len(deltas)
    print(f"\nСредняя дельта по 5 запросам: {avg_delta} секунд")

if __name__ == "__main__":
    get_time_data()