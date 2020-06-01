# Helper function used to time the solution
import time
from functools import wraps
def time_elapsed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished in {(time.perf_counter() - start_time):.5f}s")
        return result
    return wrapper

# https://en.wikipedia.org/wiki/Regular_number#Algorithms
# https://rosettacode.org/wiki/Hamming_numbers
# Ugly numbers are positive numbers whose prime factors only include 2, 3, or 5

def is_ugly(num):
    if num <= 0:
        return False    
    while num % 2 == 0: num //= 2
    while num % 3 == 0: num //= 3
    while num % 5 == 0: num //= 5
    return num == 1

# Brute Force
@time_elapsed
def hamming_brute(n):
    count = 1
    number = 1
    while count < n:
        number += 1
        if is_ugly(number):
            count += 1
    return number

@time_elapsed
def hamming(n):
    bases = [2, 3, 5]
    indexes = [0, 0, 0]
    hamming_numbers = [1]
    bag = [2, 3, 5]

    for _ in range(1, n):
        next_num = min(bag) 
        hamming_numbers.append(next_num)
        
        for i in range(3):
            if bag[i] == next_num:
                indexes[i] += 1
                bag[i] = bases[i] * hamming_numbers[indexes[i]]
    return hamming_numbers[-1]


if __name__ == "__main__":
    n = 100
    print(hamming_brute(n) == hamming(n))
