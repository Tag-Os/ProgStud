# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
# TODO здесь заполнение словаря
distances = {}

for first_city,coord1 in sites.items():
    x1 , y1 = coord1
    for second_city,coord2 in sites.items():
        if first_city != second_city:
            x2 , y2 = coord2
            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            key = "distance from " + first_city + " to " + second_city
            distances[key] = round(distance,1)
# TODO здесь вывод
for str,value in distances.items():
    print(str,value,)




