# Тестовое задание для инженера по сборке ПО

## 📌 Описание задачи
Нужно было создать 4 скрипта:
1. **`time_api.py`** — получает время с API Яндекс.Времени и замеряет задержку.
2. **`build_script.py`** — клонирует репозиторий, очищает его, создает `version.json` и архив.
3. **`version_generator.py`** — генерирует номера версий на основе шаблонов.
4. **`service_mover.sh`** — переносит systemd-юниты и обновляет их пути.

---

## 🛠 Как тестировать

### 1. Подготовка
- Установи Python 3 и Git.
- Клонируй репозиторий:
  ```bash
  git clone https://github.com/P1stak/test_task_for_software_engineer.git
  cd test_task_for_software_engineer
