# Вариант 10

## Задание

Генератор, который обходит файловую систему в указанном каталоге и
возвращает имена файлов с заданным расширением. Предусмотреть
возможность обхода подкаталогов.

## Решение задания

Задача решена с помощью библиотеки os

```python
def find_files(directory, extension):
    
    if not extension.startswith('.'):
        extension = '.' + extension

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                yield os.path.join(root, file)

```

## Вывод программы

![Ответ на задание](/lab_6/images/finder.jpg)

## Список использованных источников

1. [MarkDown](https://doka.guide/tools/markdown/ "Документация по Mark Down")
2. [Python](https://docs.python.org/3/search.html?q= "Документация по Python")
3. [Readme example](https://github.com/still-coding/report_demo "Пример для оформления работы")
