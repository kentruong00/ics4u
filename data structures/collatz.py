from functools import lru_cache
def collatz(num):
    chain = 0
    if num == 1:
        return chain
    if num % 2 == 0:
        chain += 1
        return collatz(num//2)
    
    else:
        chain += 1
        return collatz(3 * num + 1)
print(collatz(13))

@lru_cache
def collatz2(num, chain=1):
    if num == 1:
        return chain
    elif num % 2 == 0:
        return collatz2(num//2, chain + 1)
    else:
        return collatz2(3 * num + 1, chain + 1)

