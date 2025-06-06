# Тестовое задание для инженера по сборке ПО

## 📌 Описание задачи
Создать 4 скрипта:
1. **`time_api.py`** — получает время с API Яндекс.Времени и замеряет задержку
2. **`build_script.py`** — клонирует репозиторий, очищает его, создает `version.json` и архив
3. **`version_generator.py`** — генерирует номера версий на основе шаблонов
4. **`service_mover.sh`** — переносит systemd-юниты и обновляет их пути

---

## 1. Как тестировать

### 1. Подготовка
- Установите Python 3.12+ и Git
- Склонируйте репозиторий:
  ```bash
  git clone https://github.com/P1stak/test_task_for_software_engineer.git
  cd test_task_for_software_engineer
  ```
  
### 2. Тестирование скриптов

🔹 time_api.py

```bash
python time_api.py
```
Что должно вывести:
* Сырой JSON с временем
* Человекочитаемое время (например, 2025-06-06 19:13:09)
* Задержку (дельта) и среднюю задержку для 5 запросов

🔹 build_script.py

```bash
python build_script.py https://github.com/paulbouwer/hello-kubernetes.git src/app 25.3000
```
Что должно произойти:
- Клонируется репозиторий
- Удаляются все папки, кроме src/app
- Создается version.json в src/app
- Сенерируется архив app.zip

🔹 version_generator.py
- Создай config.json
 
```json
{
  "Sh1": "3.7.*",
  "Sh2": "3.*.1",
  "Sh3": "1.2.3.*"
}
```
- Запусти скрипт
```bash
python version_generator.py 3.7.5 config.json
```
Что должно вывести:
- Сгенерированные версии (например, 3.7.1, 3.7.9).
- Список версий старее 3.7.5.

🔹 service_mover.sh
```bash
sudo bash service_mover.sh
```
Что делает:
- Ищет юниты foobar-*, останавливает их.
- Переносит файлы из /opt/misc/ в /srv/data/.
- Обновляет пути в юнитах и перезапускает их.

📂 Структура репозитория
```text
test_task_for_software_engineer/
├── time_api.py            # Скрипт для работы с API времени
├── build_script.py        # Сборочный скрипт
├── version_generator.py   # Генератор версий
├── service_mover.sh       # Скрипт для systemd (Bash)
├── config.json            # Пример конфига для version_generator.py
└── README.md              # Инструкция (этот файл)
```

Проверка архива app.zip
```bash
unzip -l app.zip   # Просмотр содержимого
unzip -t app.zip   # Проверка целостности
```
