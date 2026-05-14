def find_in_nested_list(mas, num):
    """
    Ищет элемент в вложенном списке и возвращает его индекс.
    """
    stack = mas[:]
    index = 0
    while stack:
        current = stack.pop(0)
        if isinstance(current, int):
            if current == num:
                return index
            else:
                index += 1
        else:
            stack = current[:]
    return None

def calculate_sequence(u=2, v=3, k=5):
    """
    Вычисляет последовательность по заданным параметрам.
    """
    a, b = u, v
    for i in range(2, k + 1):
        a = 2 * b + a
        b = 2 * b * b + b
    return a, b