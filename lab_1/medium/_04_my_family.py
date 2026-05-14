my_family = ["Мама", "Брат", "Папа"]
my_family_height = [["Мама", 162], ["Брат", 180], ["Папа", 182]]

def run():
    print(f"Рост члена семьи {my_family[2]} - {my_family_height[2][1]}")
    total = sum(height[1] for height in my_family_height)
    print(f"Общий рост членов моей семьи - {total}")
    return total

if __name__ == "__main__":
    run()