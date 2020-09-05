"""
3. Write a program to determine if a number, given on the command line, is prime.

   1. How can you optimize this program?
   2. Implement [The Sieve of
      Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
      of the oldest algorithms known (ca. 200 BC).
"""

# Determine if a number is a prime number:
import math
#   A prime number is any number greater than 1 that is only divisable by itself and 1 (with no modulus). So given an input (n):
#        we loop through the range of numbers to get to n (starting at position 2, to bypass 0 and 1),
#         - it is assumed that n will be divisable by 1 (All positive numbers are divisable by 1)
#         - if any number between 0 and n is divisable by n, then it's not prime.
#         - if n is less than 0, it is not prime
#         - if n is only divisible by itself, it is prime, due to the assumption given above. Therefore, the number is divisible only by itself and 1 = prime


def is_prime(number):
    if number > 1:
        for position in range(2, number):
            if (number % position) == 0:
                print(number, "is not prime")
                break
        else:
            print("Yep!", number, "is prime!")
    else:
        print(number, "is not prime")
    # 1. I believe this is as optimized as it can get
##################################################################################


# 2 Sieve of Eratosthenes
  # Given an upper limit, n, determine what the prime numbers are in the range of n

# PseudoCode:
# Input a number. This will be our upper range.
# create a list from that range
# iterate through the range, and if i is in the list, we delete all of the multiples of it
# Begin Code

print('Enter a Number, and I\'ll tell you all of the Primes from 2 to that number')
number = int(input())

primes = []
for i in range(2, number + 1):
    primes.append(i)  # create a list of numbers from 2 to the upper limit


i = 2  # setting i back to 2 (the start of the array)

# From 2 to the square root of the limit, if i is in the list, we need to delete the multiples
while(i <= int(math.sqrt(number))):
    if i in primes:
        for j in range(i * 2, number + 1, i):  # j gives multiples of i starting from 2 * i
            if j in primes:  # If it's in there, we need to pull it out
                primes.remove(j)

    i = i + 1

print(primes)
