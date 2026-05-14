# Medium

Напишите для своих функций тесты с помощью pytest

## Задание 1

рекурсивный обход с использованием стека.

```python
def test_find_existing_number():
    mas = [1, 2, [3, 4, [5, [6, []]]]]
    assert find(mas, 4) == 3
```

```python
def test_find_non_existing_element():
    mas = [1, 2, [3, 4, [5, [6, []]]]]
    assert find(mas, 'spam') is None
```

## Вывод программы 1

![Ответ на задание 1](/lab_4/images/task_1_medium.jpg)

## Задание 2

проверка при k=5 какое получается значение

```python
    assert a == 3265298
    assert b == 5325028475403
```

## Вывод программы 2

![Ответ на задание 2](/lab_4/images/task_2_medium.jpg)

## Список использованных источников

1. [MarkDown](https://doka.guide/tools/markdown/ "Документация по Mark Down")
2. [Python](https://docs.python.org/3/search.html?q= "Документация по Python")
3. [Readme example](https://github.com/still-coding/report_demo "Пример для оформления работы")
