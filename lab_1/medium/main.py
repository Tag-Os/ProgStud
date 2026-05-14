# Верхнеуровневый модуль для запуска заданий 00-05

import sys
import os

# Добавляем текущую директорию в путь для импорта
sys.path.insert(0, os.path.dirname(__file__))

# Импортируем модули-задания
import _00_distance
import _01_circle
import _02_operations
import _03_favorite_movies
import _04_my_family
import _05_zoo


def main():
    print("=== Запуск заданий ===\n")
    
    # Задание 00
    print("--- Задание 00 ---")
    _00_distance.run()
    print()
    
    # Задание 01
    print("--- Задание 01 ---")
    _01_circle.run()
    print()
    
    # Задание 02
    print("--- Задание 02 ---")
    _02_operations.run()
    print()
    
    # Задание 03
    print("--- Задание 03 ---")
    _03_favorite_movies.run()
    print()
    
    # Задание 04
    print("--- Задание 04 ---")
    _04_my_family.run()
    print()
    
    # Задание 05
    print("--- Задание 05 ---")
    _05_zoo.run()
    print()
    
    print("=== Все задания выполнены ===")


if __name__ == "__main__":
    main()