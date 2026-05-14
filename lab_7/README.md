# Пакет лабораторных работ №4-6

## задание

Создайте пакет, содержащий 3 модуля на основе лабораторных работ №№
4-6
Напишите запускающий модуль на основе Typer, который позволит
выбирать и настраивать параметры запуска логики из пакета.

## Установка и запуск

1. Убедитесь, что установлен Python 3.8+.
2. Установите Typer:

   ```bash
   pip install typer
   ```

## Решение

Главный модуль реализует интерфейс командной строки (CLI) с помощью 
библиотеки Typer. Он объединяет все три модуля лабораторных работ и 
предоставляет 5 команд для вызова их функциональности с возможностью 
настройки параметров через аргументы командной строки.

```python
app = typer.Typer()  # Создание CLI-приложения

@app.command()  # Декоратор регистрирует функцию как команду
def lab4_task1(
    mas: str = typer.Option("[[1, 2], [3, [4, 5]]]", help="..."),
    num: int = typer.Option(4, help="...")
):
    # Парсинг строки в список и вызов функции из модуля lab_4
    mas_list = ast.literal_eval(mas)
    result = find_in_nested_list(mas_list, num)
    typer.echo(f"Индекс элемента {num}: {result}")
```

## примеры команд

lab4-task1: Поиск элемента во вложенном списке
lab4-task2: Вычисление последовательности
lab5-task1: Демонстрация менеджера коллекции
lab5-task2: Демонстрация декоратора
lab6-task: Поиск файлов по расширению

## пример запуска

python main.py lab4-task2 --u 1 --v 1 --k 3
![Запуск_1](/lab_7/images/test1.jpg)
python main.py lab5-task1
![Запуск_1](/lab_7/images/test2.jpg)
python main.py lab5-task2 --x 5 --y "hello" 5 hello
![Запуск_1](/lab_7/images/test3.jpg)

## Список использованных источников

1. [MarkDown](https://doka.guide/tools/markdown/ "Документация по
Mark Down")
2. [Python](https://docs.python.org/3/search.html?q= "Документация
по Python")
3. [Readme example](https://github.com/still-coding/report_demo
"Пример для оформления работы")
