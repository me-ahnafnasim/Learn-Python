#1) determine the factorial of a number

def factorial(n):
    result =1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(5))


#2) fibonacci is a series
def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        a,b =b, a+b
    return a 
print(fibonacci(7))


#3) gcd(greate common divisor)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(24,12))



#4) check a number is prime or not

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(2))


#5) Power of a number (xⁿ) using loop or recursion.
#Compute a^b using a loop.
def power(a, b):
    result =1
    for _ in range(b):
        result *=a
    return result
print(power(3,2))



#6) Sum of digits of a number
number = 12345
digits = [int(x) for x in str(number)]
print(sum(digits))

#or,

def sum_of_digits_math(n):
    n = abs(n)
    total = 0
    while n:
        total += n % 10 #get the last digit
        n //= 10 #remove the last digit
    return total
print(sum_of_digits_math(1234))






#7)  Armstrong number (also called a Narcissistic number)--(sum of digits powered by number of digits).
def is_armstrong(number):
    total = 0
    digits = []
    for d in str(number):   
        digits.append(int(d)) 
        
    len_of_digits = len(digits)  
    
    for num in digits:
        total += num ** len_of_digits
        if total == number:
            return True
    return False
print(is_armstrong(153))  # True, since 1^3 + 5^3 + 3^3 = 153
print(is_armstrong(123))  # False


#or
def is_armstrong(number):
    #first number re string bananu hoyce then proti char ke int banaye list e rakha hoyce
    digits = [int(d) for d in str(number)]  # Convert number to list(inner element is int) of digits
    num_digits = len(digits)  # Count of digits
    sum_powered_digits = sum(d ** num_digits for d in digits)  # Sum of each digit powered to num_digits
    return sum_powered_digits == number

# Example usage
print(is_armstrong(153))  # True, since 1^3 + 5^3 + 3^3 = 153
print(is_armstrong(123))  # False


#8)Reverse digits of a number (123 → 321).
number =345
n = str(number)[::-1]
print(n)

#9) count total digits in a number
number =234
digit = [int(x) for x in str(number)]
print(len(digit))


#10)Check if number is perfect/amicable/Harshad etc.
#A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
"""🚫 Not Perfect: 12
Divisors: 1, 2, 3, 4, 6
Sum: 1+2+3+4+6 = 16 ≠ 12"""

""" example: 28
Divisors: 1, 2, 4, 7, 14
Sum: 1 + 2 + 4 + 7 + 14 = 28
✅ 28 is perfect"""

def is_perfect(n):
    if n <= 1:
        return False
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum == n

# Test
print(is_perfect(6))   # True
print(is_perfect(28))  # True
print(is_perfect(12))  # False