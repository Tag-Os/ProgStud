# Есть значение радиуса круга
radius = 42

# Рассчёт и вывод площади
pi =  3.1415926
square = round(pi * radius**2,4)
print(square)

# Точка 1
point_1 = (23, 34)

result1 = (point_1[0]**2 + point_1[1]**2)**0.5 <= radius
print(result1)

# Точка 2
point_2 = (30, 30)

result2 = (point_2[0]**2 + point_2[1]**2)**0.5 <= radius
print(result2)
