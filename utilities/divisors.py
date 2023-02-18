# Divisors utilities

def divisor_counter(a):
    if a < 0:
        return
    if a == 0 or a == 1:
        return 1
    count = 1
    for i in range(2, int(a / 2) + 1):
        if a % i == 0:
            count += 1
    return count + 1
