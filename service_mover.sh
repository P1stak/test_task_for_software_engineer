#!/bin/bash

# Получаем список юнитов
units=$(systemctl list-units --all --no-legend 'foobar-*' | awk '{print $1}')

for unit in $units; do
    echo "Обработка юнита: $unit"
    
    # Останавливаем сервис
    echo "Остановка сервиса..."
    sudo systemctl stop $unit
    
    # Получаем название сервиса
    service_name=${unit#foobar-}
    
    # Старые и новые пути
    old_dir="/opt/misc/$service_name"
    new_dir="/srv/data/$service_name"
    
    # Перенос файлов
    echo "Перенос файлов из $old_dir в $new_dir"
    sudo mkdir -p $new_dir
    sudo mv $old_dir/* $new_dir/
    sudo rmdir $old_dir
    
    # Обновление юнита
    unit_file="/etc/systemd/system/$unit.service"
    echo "Обновление юнита в $unit_file"
    
    sudo sed -i "s|WorkingDirectory=$old_dir|WorkingDirectory=$new_dir|g" $unit_file
    sudo sed -i "s|ExecStart=$old_dir|ExecStart=$new_dir|g" $unit_file
    
    # Перезагрузка демона и запуск сервиса
    echo "Запуск сервиса..."
    sudo systemctl daemon-reload
    sudo systemctl start $unit
    
    echo "Юнит $unit успешно обновлен и запущен"
    echo "----------------------------------------"
done

echo "Все операции завершены"