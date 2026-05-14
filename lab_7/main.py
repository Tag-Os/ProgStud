import typer
from lab_4_module import find_in_nested_list, calculate_sequence
from lab_5_module import create_collection_manager, validate_and_call
from lab_6_module import find_files_by_extension
import os
import sys

app = typer.Typer()

@app.command()
def lab4_task1(
    mas: str = typer.Option("[[1, 2], [3, [4, 5]]]", help="Вложенный список для поиска"),
    num: int = typer.Option(4, help="Число для поиска в списке")
):
    """
    Выполняет поиск элемента в вложенном списке (Lab 4, Task 1).
    """
    try:
        # Преобразуем строку в список
        import ast
        mas_list = ast.literal_eval(mas)
        result = find_in_nested_list(mas_list, num)
        typer.echo(f"Индекс элемента {num}: {result}")
    except Exception as e:
        typer.echo(f"Ошибка: {e}")

@app.command()
def lab4_task2(
    u: int = typer.Option(2, help="Начальное значение u"),
    v: int = typer.Option(3, help="Начальное значение v"),
    k: int = typer.Option(5, help="Количество итераций")
):
    """
    Вычисляет последовательность (Lab 4, Task 2).
    """
    a, b = calculate_sequence(u, v, k)
    typer.echo(f"a = {a}, b = {b}")

@app.command()
def lab5_task1():
    """
    Демонстрирует работу с коллекцией (Lab 5, Task 1).
    """
    manager = create_collection_manager()
    manager(1, 4, 7)
    manager('sosiska')
    result = manager('stop')
    typer.echo(f"Результат коллекции: {result}")

@app.command()
def lab5_task2(
    x: int = typer.Option(1, help="Первый параметр (должен быть > 0)"),
    y: str = typer.Option("j", help="Второй параметр (должен быть строкой)")
):
    """
    Демонстрирует работу декоратора (Lab 5, Task 2).
    """
    decorated_print = validate_and_call(print)
    decorated_print(x, y)

@app.command()
def lab6_task(
    directory: str = typer.Option(".", help="Директория для поиска"),
    extension: str = typer.Option(".txt", help="Расширение файлов для поиска")
):
    """
    Находит файлы с указанным расширением (Lab 6, Task).
    """
    if not os.path.exists(directory):
        typer.echo(f"Директория {directory} не существует")
        raise typer.Exit(code=1)

    typer.echo(f"Файлы с расширением {extension} в каталоге {directory}:")
    found = False
    for file_path in find_files_by_extension(directory, extension):
        typer.echo(file_path)
        found = True

    if not found:
        typer.echo("Файлы не найдены")

if __name__ == "__main__":
    app()
