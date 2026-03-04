my_family = ["Мама", "Брат", "Папа"]

my_family_height = [
    # ['имя', рост],
    ["Мама", 162], ["Брат", 180], ["Папа", 182]
]


#   Рост отца
print("Рост члена семьи " + my_family[2], my_family_height[2][1],sep=(" - "))

#   Общий рост моей семьи
print("Общий рост членов моей семьи -", my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1])