#Write code to find factorial a given number n.

# method 1 using recursion
def factorialRecursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorialRecursive(n - 1)
ans = factorialRecursive(4)  # 4! = 4 * 3 * 2 * 1 = 24
print(ans)  

# method 2 using for loop
def factorialIterative(n):
    fact = 1
    for i in range(2,n+1):
            fact*=i
    return fact
ans2 = factorialIterative(3)  # 3! = 3 * 2 * 1 = 6
print(ans2)
