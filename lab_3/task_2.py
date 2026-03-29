nubmer = 7 * (512 ** 120) - 6 * (64 ** 100) + (8 ** 210) - 255
octal_number = oct(nubmer)[2:]
answer = octal_number.count("0")
print(answer)