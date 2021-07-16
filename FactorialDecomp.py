import time                             #https://www.codewars.com/kata/5a045fee46d843effa000070/train/python

#/************************/
# todo:
# 1.improve performance
# 2.implement solution with dict
#/************************/

primes = [2]

def decomp(n):
    result = ""
    decomposed = range(primes[0], n + 1)
    is_prime = True

    for value in decomposed:
        if primes.__contains__(value):
            continue
        for prime in primes:
            if value % prime == 0:
                #_ = value
                while value % prime == 0:
                    value /= prime
                    primes.append(prime)
                is_prime = False
                if value == 1.0:
                    break
        if is_prime:
            primes.append(value)
        is_prime = True
    temp_dict = {}
    for i in primes:
        temp_dict[i] = primes.count(i)
    for key in temp_dict:
        #if temp_dict[key] == temp_dict[-1]:
        #    result += f"{key}^{temp_dict[key]}"
        result += f"{key}^{temp_dict[key]} * "
    print(result)
    print(f"decomp:{decomposed}")
    print(f"primes:{primes}")


start = time.time()
decomp(3990)
end = time.time()
time = end - start
print(f"\nTime is {time}")
