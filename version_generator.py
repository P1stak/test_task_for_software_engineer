import json
import itertools

def generate_versions(version, config_file):
    # Чтение конфигурационного файла
    with open(config_file) as f:
        config = json.load(f)
    
    all_versions = []
    
    # Генерация версий для каждого шаблона
    for key, pattern in config.items():
        parts = pattern.split('.')
        star_indices = [i for i, part in enumerate(parts) if part == '*']
        
        if not star_indices:
            continue
        
        # Генерируем 2 варианта для каждого шаблона
        for _ in range(2):
            new_parts = parts.copy()
            for idx in star_indices:
                new_parts[idx] = str((idx + 1) * 3)  # Произвольная логика генерации
            generated_version = '.'.join(new_parts)
            all_versions.append(generated_version)
    
    # Сортировка всех версий
    sorted_versions = sorted(all_versions, key=lambda x: [int(i) for i in x.split('.')])
    
    print("Все сгенерированные версии (отсортированные):")
    for v in sorted_versions:
        print(v)
    
    # Версии старше указанной
    input_version_parts = [int(i) for i in version.split('.')]
    older_versions = []
    
    for v in sorted_versions:
        v_parts = [int(i) for i in v.split('.')]
        if v_parts < input_version_parts:
            older_versions.append(v)
    
    print("\nВерсии старше указанной:")
    for v in older_versions:
        print(v)

if __name__ == "__main__":
    # Пример вызова:
    generate_versions(
        "3.7.5",
        "config.json"
    )