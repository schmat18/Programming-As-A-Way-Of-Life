### Lab3.py Week 3 CarJus31
### Fibonacci sequence~

import math
from random import randint
n = randint(1,99999999999999999999)
#series = fibonacci

startNumber = int(raw_input("0"))
endNumber = int(raw_input("x"))

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

print map(fib, range(startNumber, endNumber))