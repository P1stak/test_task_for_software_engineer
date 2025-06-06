import os
import json
import shutil
import datetime
from git import Repo

def build_script(repo_url, src_path, version):
    print(f"[{datetime.datetime.now()}] Начало работы скрипта")
    
    # Клонирование репозитория
    print(f"[{datetime.datetime.now()}] Клонирование репозитория {repo_url}")
    repo_dir = "temp_repo"
    Repo.clone_from(repo_url, repo_dir)
    print(f"[{datetime.datetime.now()}] Репозиторий успешно клонирован")
    
    # Удаление всех директорий, кроме исходного кода
    print(f"[{datetime.datetime.now()}] Очистка ненужных директорий")
    for item in os.listdir(repo_dir):
        item_path = os.path.join(repo_dir, item)
        if item != os.path.basename(src_path) and os.path.isdir(item_path):
            shutil.rmtree(item_path)
            print(f"[{datetime.datetime.now()}] Удалена директория: {item}")
    
    # Создание version.json
    print(f"[{datetime.datetime.now()}] Создание version.json")
    src_full_path = os.path.join(repo_dir, src_path)
    files = []
    
    for root, dirs, filenames in os.walk(src_full_path):
        for f in filenames:
            if f.endswith(('.py', '.js', '.sh')):
                files.append(f)
    
    version_data = {
        "name": "hello world",
        "version": version,
        "files": files
    }
    
    version_path = os.path.join(src_full_path, "version.json")
    with open(version_path, 'w') as f:
        json.dump(version_data, f, indent=4)
    
    print(f"[{datetime.datetime.now()}] Файл version.json создан")
    
    # Создание архива
    print(f"[{datetime.datetime.now()}] Создание архива")
    last_dir = os.path.basename(src_path)
    today = datetime.datetime.now().strftime("%d%m%Y")
    archive_name = f"{last_dir}{today}.zip"
    
    shutil.make_archive(archive_name.replace('.zip', ''), 'zip', src_full_path)
    
    print(f"[{datetime.datetime.now()}] Архив {archive_name} создан")
    print(f"[{datetime.datetime.now()}] Работа скрипта завершена")

if __name__ == "__main__":
    
    # Пример вызова:
    build_script(
        "https://github.com/paulbouwer/hello-kubernetes",
        "src/app",
        "25.3000"
    )