garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# множество цветов, произрастающих в саду и на лугу,вывод всех видов
garden_set = set(garden)
meadow_set = set(meadow)
result = garden_set | meadow_set
print(result)

#те, которые растут и там и там
print(garden_set & meadow_set)
# те, которые растут в саду, но не растут на лугу
print(garden_set - meadow_set)
# те, которые растут на лугу, но не растут в саду
print(meadow_set - garden_set)