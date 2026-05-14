import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import random

class QuoteGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор цитат и фактов")
        self.root.geometry("600x400")
        
        # Инициализация БД
        self.init_database()
        
        # Создание интерфейса
        self.create_widgets()
        
    def init_database(self):
        """Создание и наполнение базы данных"""
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
        
        # Добавление тестовых данных, если таблица пуста
        self.cursor.execute('SELECT COUNT(*) FROM quotes')
        if self.cursor.fetchone()[0] == 0:
            self.insert_sample_data()
        
        self.conn.commit()
    
    def insert_sample_data(self):
        """Вставка примеров цитат и фактов"""
        quotes_data = [
            ("Будь собой, прочие роли уже заняты.", "Оскар Уайльд", "quote"),
            ("Жизнь - это то, что происходит с нами, пока мы строим планы.", "Джон Леннон", "quote"),
            ("Успех - это способность шагать от одной неудачи к другой, не теряя энтузиазма.", "Уинстон Черчилль", "quote"),
            ("Вода - единственное вещество на Земле, которое существует в трех агрегатных состояниях.", "Наука", "fact"),
            ("Человеческий мозг генерирует около 70 000 мыслей в день.", "Наука", "fact"),
            ("Кошки спят примерно 16 часов в сутки.", "Животные", "fact"),
            ("Солнце настолько велико, что в него поместится 1.3 миллиона планет размером с Землю.", "Космос", "fact")
        ]
        
        self.cursor.executemany(
            'INSERT INTO quotes (text, author, type) VALUES (?, ?, ?)',
            quotes_data
        )
    
    def create_widgets(self):
        """Создание элементов интерфейса"""
        # Заголовок
        title_label = ttk.Label(
            self.root, 
            text="Генератор цитат и фактов", 
            font=('Arial', 16, 'bold')
        )
        title_label.pack(pady=10)
        
        # Тип контента
        type_frame = ttk.Frame(self.root)
        type_frame.pack(pady=10)
        
        ttk.Label(type_frame, text="Тип:").pack(side=tk.LEFT, padx=5)
        
        self.type_var = tk.StringVar(value="all")
        ttk.Radiobutton(
            type_frame, text="Все", variable=self.type_var, value="all"
        ).pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(
            type_frame, text="Цитаты", variable=self.type_var, value="quote"
        ).pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(
            type_frame, text="Факты", variable=self.type_var, value="fact"
        ).pack(side=tk.LEFT, padx=5)
        
        # Кнопка генерации
        generate_btn = ttk.Button(
            self.root, 
            text="Сгенерировать", 
            command=self.generate_quote
        )
        generate_btn.pack(pady=20)
        
        # Область отображения
        self.result_text = tk.Text(
            self.root, 
            height=10, 
            width=60, 
            font=('Arial', 11),
            wrap=tk.WORD
        )
        self.result_text.pack(pady=10, padx=20)
        
        # Кнопка добавления
        add_btn = ttk.Button(
            self.root, 
            text="Добавить свою цитату/факт", 
            command=self.open_add_window
        )
        add_btn.pack(pady=10)
    
    def generate_quote(self):
        """Генерация случайной цитаты или факта"""
        quote_type = self.type_var.get()
        
        if quote_type == "all":
            self.cursor.execute('SELECT text, author, type FROM quotes ORDER BY RANDOM() LIMIT 1')
        else:
            self.cursor.execute(
                'SELECT text, author, type FROM quotes WHERE type = ? ORDER BY RANDOM() LIMIT 1',
                (quote_type,)
            )
        
        result = self.cursor.fetchone()
        
        if result:
            text, author, qtype = result
            self.result_text.delete(1.0, tk.END)
            
            if qtype == "quote" and author:
                self.result_text.insert(1.0, f"«{text}»\n\n— {author}")
            else:
                self.result_text.insert(1.0, f"Факт: {text}\n\nКатегория: {author}")
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(1.0, "Нет доступных записей для выбранного типа.")
    
    def open_add_window(self):
        """Открытие окна добавления новой записи"""
        add_window = tk.Toplevel(self.root)
        add_window.title("Добавить запись")
        add_window.geometry("400x300")
        
        # Тип записи
        ttk.Label(add_window, text="Тип записи:").pack(pady=5)
        type_var = tk.StringVar(value="quote")
        ttk.Radiobutton(
            add_window, text="Цитата", variable=type_var, value="quote"
        ).pack()
        ttk.Radiobutton(
            add_window, text="Факт", variable=type_var, value="fact"
        ).pack()
        
        # Текст
        ttk.Label(add_window, text="Текст:").pack(pady=5)
        text_entry = tk.Text(add_window, height=5, width=40)
        text_entry.pack(pady=5)
        
        # Автор/Категория
        ttk.Label(add_window, text="Автор/Категория:").pack(pady=5)
        author_entry = ttk.Entry(add_window, width=40)
        author_entry.pack(pady=5)
        
        def save_entry():
            text = text_entry.get("1.0", tk.END).strip()
            author = author_entry.get().strip()
            entry_type = type_var.get()
            
            if not text:
                messagebox.showwarning("Предупреждение", "Введите текст!")
                return
            
            self.cursor.execute(
                'INSERT INTO quotes (text, author, type) VALUES (?, ?, ?)',
                (text, author if author else None, entry_type)
            )
            self.conn.commit()
            
            messagebox.showinfo("Успех", "Запись добавлена!")
            add_window.destroy()
        
        ttk.Button(add_window, text="Сохранить", command=save_entry).pack(pady=10)
    
    def __del__(self):
        """Закрытие соединения с БД при завершении"""
        if hasattr(self, 'conn'):
            self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteGenerator(root)
    root.mainloop()