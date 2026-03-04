zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

zoo.insert(1,"bear")
print(zoo)

birds = ['rooster', 'ostrich', 'lark', ]

zoo += birds
print(zoo)

zoo.remove("elephant")
print(zoo)

print("Номер клетки льва:",zoo.index("lion") + 1)
print("Номер клетки жаворонка:",zoo.index("lark") + 1)
