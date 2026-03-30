u = 2
v = 3
k = 5

a, b = u, v

for i in range(2, k + 1):
    a = 2 * b + a
    b = 2 * b * b + b
print(f"a = {a}, b = {b}")
    