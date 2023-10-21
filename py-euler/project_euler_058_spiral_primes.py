"""
    Spiral Primes

    Problem 58

    Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49

    It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting
    is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

    If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.
    If this process is continued, what is the side length of the square spiral for which the ratio of primes along
    both diagonals first falls below 10%?

"""
import utilities.primes as pr

debug = True

max_num = 2 * 10 ** 8
pp = pr.PrimeProcessor(max_num)
prime_list = pp.primes_up_to(max_num)


def get_answer():
    global prime_list

    local_prime_index = 0
    local_prime_list = prime_list[local_prime_index:local_prime_index + 10000]
    local_prime_cut_off = local_prime_list[-1:][0]

    diag_nums = [1]
    ratio = 1
    prime_count = 0.0
    num_count = 1.0
    i = 2
    # 3,5,7,9
    # 13,17,21,25
    # 31,37,43,49
    while ratio > 0.10:
        nums_to_append = [diag_nums[-1:][0] + i * j for j in range(1,5)]

        if nums_to_append[3] > local_prime_cut_off:
            local_prime_index += 5000
            local_prime_list = prime_list[local_prime_index:max(len(prime_list) - 1, local_prime_index + 10000)]
            if len(local_prime_list) == 0:
                print(f'Ran out of primes!!! Max prime = {prime_list[-1:][0]}')
            local_prime_cut_off = local_prime_list[-1:][0]

        diag_nums += nums_to_append
        num_count += 4.0
        prime_count += sum([1 for num in nums_to_append if num in local_prime_list])
        ratio = prime_count / num_count
        i += 2

        if debug and i % 100 == 0:
            print(f'{int(prime_count)}/{int(num_count)} = {ratio}, max diagonal num considered: {nums_to_append[3]}')

    return i


def main():
    answer = get_answer()
    print(f"The Answer to Project Euler 058 is {answer}")

    # The Answer to Project Euler 058 is __


if __name__ == "__main__":
    main()
