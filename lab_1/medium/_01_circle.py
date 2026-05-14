radius = 42
pi = 3.1415926

def run():
    square = round(pi * radius ** 2, 4)
    print(square)
    
    point_1 = (23, 34)
    result1 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5 <= radius
    print(result1)
    
    point_2 = (30, 30)
    result2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5 <= radius
    print(result2)
    
    return square, result1, result2

if __name__ == "__main__":
    run()