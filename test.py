"""
test.py - Тестирование функций из модуля lib.py
"""

import sys
import os

# Добавляем текущую директорию в путь для импорта
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lib import count_common_elements, find_common_elements, count_element_frequency

def test_basic_functionality():
    """Тестирование базовой функциональности"""
    print("=== Тестирование базовой функциональности ===")
    
    # Тест 1: Обычный случай
    result1 = count_common_elements([1, 2, 3], [2, 3, 4], [3, 4, 5])
    expected1 = 1
    print(f"Тест 1: {result1} == {expected1} {'✓' if result1 == expected1 else '✗'}")
    
    # Тест 2: Все элементы общие
    result2 = count_common_elements([1, 2], [1, 2], [1, 2])
    expected2 = 2
    print(f"Тест 2: {result2} == {expected2} {'✓' if result2 == expected2 else '✗'}")
    
    # Тест 3: Нет общих элементов
    result3 = count_common_elements([1, 2], [3, 4], [5, 6])
    expected3 = 0
    print(f"Тест 3: {result3} == {expected3} {'✓' if result3 == expected3 else '✗'}")
    
    # Тест 4: Один список
    result4 = count_common_elements([1, 2, 3])
    expected4 = 3
    print(f"Тест 4: {result4} == {expected4} {'✓' if result4 == expected4 else '✗'}")
    
    # Тест 5: Пустые списки
    result5 = count_common_elements([], [], [])
    expected5 = 0
    print(f"Тест 5: {result5} == {expected5} {'✓' if result5 == expected5 else '✗'}")

def test_find_common_elements():
    """Тестирование функции find_common_elements"""
    print("\n=== Тестирование find_common_elements ===")
    
    # Тест 1: Числа
    result1 = find_common_elements([1, 2, 3], [2, 3, 4], [3, 4, 5])
    expected1 = {3}
    print(f"Тест 1: {result1} == {expected1} {'✓' if result1 == expected1 else '✗'}")
    
    # Тест 2: Строки
    result2 = find_common_elements(['a', 'b'], ['b', 'c'], ['b', 'd'])
    expected2 = {'b'}
    print(f"Тест 2: {result2} == {expected2} {'✓' if result2 == expected2 else '✗'}")
    
    # Тест 3: Смешанные типы
    result3 = find_common_elements([1, 'a', 3], [1, 'a', 4], [1, 'a', 5])
    expected3 = {1, 'a'}
    print(f"Тест 3: {result3} == {expected3} {'✓' if result3 == expected3 else '✗'}")

def test_edge_cases():
    """Тестирование граничных случаев"""
    print("\n=== Тестирование граничных случаев ===")
    
    # Тест 1: Один пустой список
    result1 = count_common_elements([1, 2, 3], [])
    expected1 = 0
    print(f"Тест 1: {result1} == {expected1} {'✓' if result1 == expected1 else '✗'}")
    
    # Тест 2: Дубликаты в списках
    result2 = count_common_elements([1, 1, 2, 2], [1, 2, 2, 3], [1, 1, 1, 2])
    expected2 = 2  # Уникальные общие элементы: 1 и 2
    print(f"Тест 2: {result2} == {expected2} {'✓' if result2 == expected2 else '✗'}")
    
    # Тест 3: Большие списки
    result3 = count_common_elements(list(range(100)), list(range(50, 150)), list(range(25, 75)))
    expected3 = 25  # Общие элементы: 50-74
    print(f"Тест 3: {result3} == {expected3} {'✓' if result3 == expected3 else '✗'}")

def run_all_tests():
    """Запуск всех тестов"""
    print("Запуск тестов модуля lib.py")
    print("=" * 50)
    
    test_basic_functionality()
    test_find_common_elements()
    test_edge_cases()
    
    print("\n" + "=" * 50)
    print("Тестирование завершено!")

if __name__ == "__main__":
    run_all_tests()