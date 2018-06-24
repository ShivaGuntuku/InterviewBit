# http://wwwhomes.uni-bielefeld.de/achim/prime_sieve.html
# A = 1048574
# s=  [num for num in range(2,A) if all(num%i!=0 for i in range(2,num))]
# print [[s[i],s[j]] for i in range(len(s)) for j in range(len(s)) if s[i]+s[j] == A]
# print s


# Python program to print all primes smaller than or equal to
# n using Sieve of Eratosthenes

n=1048574
prime = [True for i in range(n+1)]
p = 2
while (p * p <= n):
    if (prime[p] == True):
        for i in range(p * 2, n+1, p):
            prime[i] = False
    p += 1
s = [p for p in range(2, n) if prime[p]]
for i in s:
    if n-i in s:
        print i,n-i
        break 




