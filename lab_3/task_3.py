import math

def count_divisors(n):
    count = 0
    limit = math.isqrt(n)
    for i in range(1, limit + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count

max_divisors = 0
result_number = 0

for num in range(84052, 84131): 
    divisor_count = count_divisors(num)

    if divisor_count > max_divisors:
        max_divisors = divisor_count
        result_number = num


print(max_divisors, result_number)