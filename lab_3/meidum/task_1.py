def counter():
    """
    Возвращает количество 5-буквенных комбинаций из букв ['И', 'В', 'А', 'Н'],
    содержащих хотя бы одну букву 'И'.

    >>> counter()
    781

    Проверка на маленькой длине (2 буквы, алфавит ['И', 'В']):
    >>> def small_counter():
    ...     letters = ['И', 'В']
    ...     count = 0
    ...     def generate(current):
    ...         nonlocal count
    ...         if len(current) == 2:
    ...             if 'И' in current:
    ...                 count += 1
    ...             return
    ...         for letter in letters:
    ...             generate(current + letter)
    ...     generate("")
    ...     return count
    ...
    >>> small_counter()  # Все комбинации: ИИ, ИВ, ВИ, ВВ. Без И только ВВ -> 3
    3

    Проверка, что результат целое положительное число:
    >>> isinstance(counter(), int)
    True
    >>> counter() > 0
    True
    """
    letters = ['И', 'В', 'А', 'Н']
    count = 0
    
    def generate(current):
        nonlocal count
        if len(current) == 5:
            if 'И' in current:
                count += 1
            return
        
        for letter in letters:
            generate(current + letter)
    
    generate("")
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)