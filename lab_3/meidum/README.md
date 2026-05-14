# Medium

## Задание

Напишите для функций доктесты

## Описание

task_1.py
Логика: Рекурсивный перебор всех 5-буквенных комбинаций из букв 
['И', 'В', 'А', 'Н'] (всего 4^5 = 1024 комбинации). Подсчитываются 
только те комбинации, которые содержат хотя бы одну букву 'И'.

```python
def generate(current):
    if len(current) == 5:
        if 'И' in current:
            count += 1
        return
    
    for letter in letters:
        generate(current + letter)
```

task_2.py
Логика: Вычисляется арифметическое выражение 7 * (512 ** 120) - 6 * (64 ** 100) + (8 ** 210) - 255. Затем результат переводится в восьмеричную систему счисления, и подсчитывается количество нулей в этой записи.

```python
number = 7 * (512 ** 120) - 6 * (64 ** 100) + (8 ** 210) - 255
octal_number = oct(number)[2:]
answer = octal_number.count("0")
```

task_3.py
Логика: В диапазоне чисел от 84052 до 84130 (включительно) ищется число с максимальным количеством натуральных делителей. Для каждого числа подсчитываются делители (оптимизировано через math.isqrt, чтобы не перебирать до самого числа).

```python
for num in range(84052, 84131):
    divisor_count = count_divisors(num)
    
    if divisor_count > max_divisors:
        max_divisors = divisor_count
        result_number = num
```

## Вывод тестов

task_1
![Запуск_1](/lab_3/images/task_1_medium.jpg)
task_2
![Запуск_1](/lab_3/images/task_2_medium.jpg)
task_3
![Запуск_1](/lab_3/images/task_3_medium.jpg)

## Список использованных источников

1. [MarkDown](https://doka.guide/tools/markdown/ "Документация по Mark Down")
2. [Python](https://docs.python.org/3/search.html?q= "Документация по Python")
3. [Readme example](https://github.com/still-coding/report_demo "Пример для оформления работы")
