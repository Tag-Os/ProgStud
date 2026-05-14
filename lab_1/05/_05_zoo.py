def run():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    zoo.insert(1, "bear")
    print(zoo)
    
    birds = ['rooster', 'ostrich', 'lark']
    zoo += birds
    print(zoo)
    
    zoo.remove("elephant")
    print(zoo)
    
    lion_cell = zoo.index("lion") + 1
    lark_cell = zoo.index("lark") + 1
    print(f"Номер клетки льва: {lion_cell}")
    print(f"Номер клетки жаворонка: {lark_cell}")
    
    return lion_cell, lark_cell

if __name__ == "__main__":
    run()
