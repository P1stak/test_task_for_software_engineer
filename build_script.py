import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import os
import shutil
import json
from datetime import datetime
import subprocess

def build_script(repo_url, src_path, version):
    print(f"[{datetime.now()}] Начало работы скрипта")
    
    # 1. Клонирование репозитория
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    repo_path = f"temp_repo_{repo_name}"
    print(f"[{datetime.now()}] Клонирование репозитория {repo_url}")
    subprocess.run(["git", "clone", repo_url, repo_path], check=True)
    
    # 2. Определяем, какие папки нужно сохранить (src_path)
    src_dir = src_path.split("/")[0]  # "src" из "src/app"
    print(f"[{datetime.now()}] Очистка ненужных директорий (кроме {src_dir})")
    
    # 3. Удаляем всё, кроме нужной папки (src)
    for item in os.listdir(repo_path):
        item_path = os.path.join(repo_path, item)
        if item == src_dir:
            continue  # Не удаляем папку с исходным кодом
        if os.path.isdir(item_path):
            print(f"[{datetime.now()}] Удалена директория: {item}")
            shutil.rmtree(item_path, ignore_errors=True)
    
    # 4. Создаём version.json внутри src/app
    version_dir = os.path.join(repo_path, src_path)
    os.makedirs(version_dir, exist_ok=True)  # Создаём папки, если их нет
    
    version_path = os.path.join(version_dir, "version.json")
    files = [
        f for f in os.listdir(version_dir)
        if f.endswith((".py", ".js", ".sh"))
    ]
    
    version_data = {
        "name": "hello world",
        "version": version,
        "files": files
    }
    
    print(f"[{datetime.now()}] Создание version.json в {version_path}")
    with open(version_path, "w") as f:
        json.dump(version_data, f, indent=4)
    
    # 5. Создаём архив
    archive_base = src_path.split("/")[-1]  # "app"
    archive_name = f"{archive_base}{datetime.now().strftime('%Y%m%d')}.zip"
    print(f"[{datetime.now()}] Создание архива {archive_name}")
    shutil.make_archive(archive_base, "zip", version_dir)
    
    # 6. Удаляем временную папку (опционально)
    shutil.rmtree(repo_path, ignore_errors=True)
    print(f"[{datetime.now()}] Готово! Архив: {archive_name}")

if __name__ == "__main__":
    build_script(
        "https://github.com/paulbouwer/hello-kubernetes.git",
        "src/app",
        "25.3000"
    )