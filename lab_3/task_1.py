def counter():
    letters = ['И', 'В', 'А', 'Н']
    count = 0
    
    def generate(current):
        nonlocal count
        if len(current) == 5:
            if 'И' in current:
                count += 1
            return
        
        for letter in letters:
            generate(current + letter)
    
    generate("")
    return count

result = counter()
print(result)