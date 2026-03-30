# Вариант 10

Функция для поиска значения в сложном объекте

## Задание 1

```python
>>> find([1, 2, [3, 4, [5, [6, []]]]], 4)
3
>>> find([1, 2, [3, 4, [5, [6, []]]]], 'spam'])
None
```

## Решение задания 1 (Без рекурсии)

Задача была решена с помощью цикла "While",вот основной кусок:

```python
def find (mas,num):
    stack = mas[:]
    index = 0
    answer = None
    while stack:
        current = stack.pop(0)
        if isinstance(current,int):
            if current == num:
                return(index)
            else:index += 1
        else:
            stack = current[:]

    return(answer)
```

## Вывод программы 1 (Без рекурсии)

![Ответ на задание 1](/lab_4/images/task_1_answer.jpg)

## Решение задания 1 (рекурсия)

Задача решена с помощью многочисленных вызовов функции саму себя,а также проверки типа данных при помощи "isinstance"

```python
def find (mas,number):
    for i in range (len(mas)):
        if  isinstance(mas[i],list):
            result = find(mas[i],number) 
            if isinstance(result,int):
                return(result + i)
        else:
            if mas[i] == number:return(i)
    
    return
```

## Вывод программы 1(рекурсия)

![Ответ на задание 1 рекурсия](/lab_4/images/task_1_answer(rec).jpg)

## Задание 2

Функция для расчёта

## Решение задания 2(без рекурсии)

Вся задача решена с помощью цикла "for"

```python
for i in range(2, k + 1):
    a = 2 * b + a
    b = 2 * b * b + b
print(f"a = {a}, b = {b}")
```

## Вывод программы 2 (без рекурсии)

![Ответ на задание 2 без рекурсии](/lab_4/images/task_2_answer.jpg)

## Решение задания 2(рекурсия)

Основной код для реекурсивного метода

```python
def calculate_ab(k, u, v):
    if k == 1:
        return u, v
    else:
        a_prev, b_prev = calculate_ab(k - 1, u, v)
        a = 2 * b_prev + a_prev
        b = 2 * b_prev * b_prev + b_prev
        return a, b
```

## Вывод программы 2 (рекурсия)

![Ответ на задание 2 без рекурсии](/lab_4/images/task_2_answer(rec).jpg)

## Список использованных источников

1. [MarkDown](https://doka.guide/tools/markdown/ "Документация по Mark Down")
2. [Python](https://docs.python.org/3/search.html?q= "Документация по Python")
3. [Readme example](https://github.com/still-coding/report_demo "Пример для оформления работы")
