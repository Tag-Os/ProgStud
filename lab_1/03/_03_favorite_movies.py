my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

def run():
    print(my_favorite_movies[:10])
    print(my_favorite_movies[-15:])
    print(my_favorite_movies[12:25])
    print(my_favorite_movies[-22:-17])
    return [my_favorite_movies[:10], my_favorite_movies[-15:], my_favorite_movies[12:25], my_favorite_movies[-22:-17]]

if __name__ == "__main__":
    run()