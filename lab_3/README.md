# Вариант 10

## Задание 1

Иван составляет 5-буквенные коды из букв И, В, А, Н. Буквы в коде могут повторяться, использовать все буквы не обязательно, но букву И нужно использовать хотя бы один раз. Сколько различных кодов может составить Иван?

## Решение задания 1

Задача решена с помощью вложенных функций def

```python
def counter():
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
```

## Вывод программы 1

![Ответ на задание 1](/lab_3/images/task_1_result.jpg)

## Задание 2

Значение арифметического выражения
$$7 \cdot 512 - \frac{120}{6} \cdot 64 + \frac{100}{8} \cdot 210 - 255$$
записали в системе счисления с основанием 8. Сколько цифр 0 содержится в этой записи?

## Решение задания 2

С помощью python провёл все вычисления,а после вывел результат.

```python
nubmer = 7 * (512 ** 120) - 6 * (64 ** 100) + (8 ** 210) - 255
octal_number = oct(nubmer)[2:]
answer = octal_number.count("0")
print(answer)
```

## Вывод программы 2

![Ответ на задание 2](/lab_3/images/task_2_result.jpg)

## Задание 3

Найдите среди целых чисел, принадлежащих числовому отрезку [84052; 84130], число, имеющее максимальное количество различных натуральных делителей, если таких чисел несколько  — найдите минимальное из них. Выведите на экран количество делителей такого числа и само число.

Например, в диапазоне [2; 48] максимальное количество различных натуральных делителей имеет число 48, поэтому для этого диапазона вывод на экране должна содержать следующие значения:

## Решение задания 3

Отдельно создана функция для подсчёта делителей:

```python
def count_divisors(n):
    count = 0
    limit = math.isqrt(n)
    for i in range(1, limit + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count
```

Затем с помощью цикла for перебрал все числа и нашёл необходимое.

```python
for num in range(84052, 84131): 
    divisor_count = count_divisors(num)

    if divisor_count > max_divisors:
        max_divisors = divisor_count
        result_number = num

print(max_divisors, result_number)
```

## Вывод программы 3

![Ответ на задание 3](/lab_3/images/task_3_result.jpg)

## Список использованных источников

1. [MarkDown](https://doka.guide/tools/markdown/ "Документация по Mark Down")
2. [Python](https://docs.python.org/3/search.html?q= "Документация по Python")
3. [Readme example](https://github.com/still-coding/report_demo "Пример для оформления работы")
