def count_common_elements(*lists):
    """
    Функция принимает на вход N списков и возвращает количество одинаковых элементов в них.
    
    Args:
        *lists: произвольное количество списков
    
    Returns:
        int: количество элементов, которые присутствуют во всех переданных списках
    """
    if not lists:
        return 0
    
    # Находим пересечение всех множеств
    common_elements = set(lists[0])
    for lst in lists[1:]:
        common_elements = common_elements.intersection(set(lst))
    
    return len(common_elements)