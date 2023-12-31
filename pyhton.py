# Exercise 1 - Write a program that prints out given sequence
# 1 3 5 11 13 15 17 19 23 25 29 31 33 37 39 41 ... 100

def print_sequence():
    sequence = [1, 3, 5]
    num = 5
    while num <= 100:
        num += 6
        sequence.append(num - 2)
        sequence.append(num)
    for num in sequence:
        print(num, end=" ")

print_sequence() # 

# Exercise 2 - Write a function, that will print the numbers for the following equation till they reach to 1.
#         | x/2  , x is even
#  f(x) = |
#         | 3x+1 , x is odd
# If x = 7, the output will be : 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1

# Exercise 3 -
# Euclid's formula is a fundamental formula for generating Pythagorean triples.
# Given an arbitrary pair of integers m and n with m > n > 0.
# The triple generated by Euclid's formula is primitive "if and only if m and n are coprime" and not both odd.
# The formula states that the integers
# a = m^2 - n^2
# b = 2*m*n
# c = m^2 + n^2
# Write a program that prints out primitive Pythagorean triple that is smaller than 100.
# Write the gcd function by yourself.
# Expected output given below;
# 3 4 5
# 5 12 13
# 15 8 17
# 7 24 25
# 21 20 29
# 9 40 41
# 35 12 37
# 11 60 61
# 45 28 53
# 33 56 65
# 13 84 85
# 63 16 65
# 55 48 73
# 39 80 89
# 77 36 85
# 65 72 97

# Exercise 4 - Write a "recursive" countdown program starting from an integer n value
# If n = 3, the output will be
# 3
# 2
# 1
# 0
# Finished