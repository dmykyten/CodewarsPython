import time                             #https://www.codewars.com/kata/5a045fee46d843effa000070/train/python

primes = [2]

def decomp(n):
    decomposed = range(primes[0], n + 1)
    get_primes(decomposed)
    for prime in primes:
        for value in decomposed:
            pass
    pass


def get_primes(_range):

    is_prime = True
    for value in _range:

        if primes.__contains__(value):
            continue

        for prime in primes:
            if value % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(value)
        is_prime = True


start = time.time()
decomp(4000)
end = time.time()
time = end - start
print(f"\nTime is {time}")
