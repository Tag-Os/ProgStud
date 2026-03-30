def calculate_ab(k, u, v):
    if k == 1:
        return u, v
    else:
        a_prev, b_prev = calculate_ab(k - 1, u, v)
        a = 2 * b_prev + a_prev
        b = 2 * b_prev * b_prev + b_prev
        return a, b

u = 2
v = 3
k = 5

for i in range(1, k + 1):
    a, b = calculate_ab(i, u, v)
print(f"a = {a}, b = {b}")