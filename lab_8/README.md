# Вариант 10

## Задание

Генератор цитат/фактов с GUI на Tkinter.
Medium — добавлена интеграция с базой данных SQLite.

## Решение задания

Задача решена с использованием объектно-ориентированного подхода.
Создан класс QuoteGenerator, который инкапсулирует всю логику
приложения.

Структура базы данных:

```python
def init_database(self):
    self.conn = sqlite3.connect('quotes.db')
    self.cursor = self.conn.cursor()
    
    self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            author TEXT,
            type TEXT NOT NULL
        )
    ''')
```

База данных состоит из одной таблицы quotes с полями:

1. id — уникальный идентификатор (автоинкремент)
2. text — текст цитаты или факта
3. author — автор цитаты или категория факта
4. type — тип записи (quote или fact)

Наполнение начальными данными:

```python
def insert_sample_data(self):
    quotes_data = [
        ("Будь собой, прочие роли уже заняты.", "Оскар Уайльд", "quote"),
        ("Вода - единственное вещество на Земле...", "Наука", "fact"),
        # ...
    ]
    
    self.cursor.executemany(
        'INSERT INTO quotes (text, author, type) VALUES (?, ?, ?)',
        quotes_data
    )
```

При первом запуске таблица автоматически наполняется тестовыми
данными, если она пуста.

Генерация случайной записи:

```python
def generate_quote(self):
    quote_type = self.type_var.get()
    
    if quote_type == "all":
        self.cursor.execute(
            'SELECT text, author, type FROM quotes ORDER BY RANDOM() LIMIT 1'
        )
    else:
        self.cursor.execute(
            'SELECT text, author, type FROM quotes WHERE type = ? ORDER BY RANDOM() LIMIT 1',
            (quote_type,)
        )
```

## Вывод программы 1

![интерфейс](/lab_8/images/for_readme_generator.jpg)
![интерфейс с цитатой](/lab_8/images/for_readme_generator_work.jpg)

## Список использованных источников

1. [MarkDown](https://doka.guide/tools/markdown/ "Документация по Mark Down")
2. [Python](https://docs.python.org/3/search.html?q= "Документация по Python")
3. [Readme example](https://github.com/still-coding/report_demo "Пример для оформления работы")