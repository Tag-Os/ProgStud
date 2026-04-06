# Вариант 10

## Задание 1

Замыкание для накопления всех аргументов в коллекции, при получении определённого значения - возврат и очистка коллекции.

## Решение задания 1

Задача решена с помощью замыкания

```python
def make_collection():
    collection = []
    def change_collection(*new_collection):
        if new_collection[0] == "stop":
            result = collection.copy()  
            collection.clear()          
            return result
        else:
            collection.extend(new_collection)
    return change_collection
test = make_collection()

test(1,4,7)
test('sosiska')
print(test('stop'))
```

## Вывод программы 1

![Ответ на задание 1](/lab_5/images/task_1_result.jpg)

## Задание 2

Декоратор для валидации аргументов функции с помощью условий:

```python
@validate(lambda x: x > 0, lambda y: isinstance(y, str))
def my_function(x, y):
    pass
```

## Решение задания 2

С помощью декоратора выполнил задание:

```python
def decorator(func):
    def validation (x,y):
        if x > 0 and isinstance(y,str):
            return func(x, y)
        else:
            return func("incorrect")
    return validation

cheсk = decorator(print)
cheсk(1,"j")
cheсk(-4,"j")
```

## Вывод программы 2

![Ответ на задание 2](/lab_5/images/task_2_result.jpg)

## Список использованных источников

1. [MarkDown](https://doka.guide/tools/markdown/ "Документация по Mark Down")
2. [Python](https://docs.python.org/3/search.html?q= "Документация по Python")
3. [Readme example](https://github.com/still-coding/report_demo "Пример для оформления работы")
