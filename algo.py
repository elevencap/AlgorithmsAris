# Array Mathematics
import numpy

n, m = map(int, input().split())

a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)

print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(numpy.floor_divide(a, b))
print(numpy.mod(a, b))
print(numpy.power(a, b))


# Eye and Identity
import numpy
numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())
print(numpy.eye(n, m))


# Concatenate
import numpy

n, m, p = map(int, input().split())

array_1_list = []
for _ in range(n):
    array_1_list.append(input().split())
array_1 = numpy.array(array_1_list, int)

array_2_list = []
for _ in range(m):
    array_2_list.append(input().split())
array_2 = numpy.array(array_2_list, int)

print(numpy.concatenate((array_1, array_2), axis=0))



# Transpose and Flatten
import numpy

n, m = map(int, input().split())
temp_list = []
for _ in range(n):
    temp_list.append(input().split())
my_array = numpy.array(temp_list, int)
print(numpy.transpose(my_array))
print(my_array.flatten())



# Shape and Reshape
import numpy

nums = list(map(int, input().split()))
print(numpy.reshape(nums, (3, 3)))


# Arrays
import numpy


def arrays(arr):
    a = numpy.array(arr, float)
    return a[::-1]


# collections.Counter()
import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    counts = Counter(s)
    sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    for char, count in sorted_chars[:3]:
        print(char, count)  


# Floor, Ceil and Rint
import numpy
numpy.set_printoptions(legacy='1.13')

a = numpy.array(input().split(), float)

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))


# Collections.deque()
from collections import deque

d = deque()
for _ in range(int(input())):
    op = input().split()
    if op[0] == 'append':
        d.append(op[1])
    elif op[0] == 'appendleft':
        d.appendleft(op[1])
    elif op[0] == 'pop':
        d.pop()
    elif op[0] == 'popleft':
        d.popleft()

print(*(d))



# Word Order
from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    word = input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(len(d))
print(*(d.values()))



# Company Logo
from collections import OrderedDict

n = int(input())
oggetti = OrderedDict()

for _ in range(n):
    *nome_pezzi, prezzo = input().split()
    nome_item = " ".join(nome_pezzi)
    prezzo = int(prezzo)
    
    if nome_item in oggetti:
        oggetti[nome_item] += prezzo
    else:
        oggetti[nome_item] = prezzo

for nome, prezzo_totale in oggetti.items():
    print(f"{nome} {prezzo_totale}")


# Collections.Ordered Dict()
from collections import OrderedDict

n = int(input())
oggetti = OrderedDict()

for _ in range(n):
    *nome_pezzi, prezzo = input().split()
    nome_item = " ".join(nome_pezzi)
    prezzo = int(prezzo)
    
    if nome_item in oggetti:
        oggetti[nome_item] += prezzo
    else:
        oggetti[nome_item] = prezzo

for nome, prezzo_totale in oggetti.items():
    print(f"{nome} {prezzo_totale}")



# DefaultDict Tutorial
from collections import defaultdict

n, m = map(int, input().split())

dizionario_a = defaultdict(list)

for i in range(1, n + 1):
    parola = input()
    dizionario_a[parola].append(i)

for _ in range(m):
    parola = input()
    if parola in dizionario_a:
        print(*(dizionario_a[parola]))
    else:
        print(-1)


# collections.Counter() (Py-Shoes)
from collections import Counter

num_scarpe = int(input())
taglie_scarpe = list(map(int, input().split()))
num_clienti = int(input())


inventario = Counter(taglie_scarpe)

incasso_totale = 0


for _ in range(num_clienti):
    taglia, prezzo = map(int, input().split())
    

    if inventario[taglia] > 0:
        incasso_totale += prezzo
        inventario[taglia] -= 1

print(incasso_totale)



# String Formatting
def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(
            str(i).rjust(width),
            oct(i)[2:].rjust(width),
            hex(i)[2:].upper().rjust(width),
            bin(i)[2:].rjust(width)
        )


# Designer Door Mat
N, M = map(int, input().split())

for i in range(1, N, 2):
    print((".|." * i).center(M, "-"))

print("WELCOME".center(M, "-"))

for i in range(N - 2, -1, -2):
    print((".|." * i).center(M, "-"))


# Text Wrap
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)




# String Validators
if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))



# Find a string
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count


# What's Your Name?
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")


# String Split and Join
def split_and_join(line):
    a = line.split(" ")
    return "-".join(a)

# SWAP CASE
def swap_case(s):
    output = []
    for char in s:
        if char.islower():
            output.append(char.upper())
        elif char.isupper():
            output.append(char.lower())
        else:
            output.append(char)
    return ''.join(output)



# Nested Lists
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores


# Finding the percentage
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())

# Mutations
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

# Say "Hello, World!" With Python
print("Hello, World!")


# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)


# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)


# Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i * i)


# Write a function
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap


# Print Function
if __name__ == '__main__':
    n = int(input())
    print(*(range(1, n + 1)), sep='')


# Python If-Else
if __name__ == '__main__':
    n = int(input())
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")


# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(result)


# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])


# Collections.namedtuple()
from collections import namedtuple
n = int(input())
fields = input().split()
Student = namedtuple('Student', fields)
total = sum([int(Student(*input().split()).MARKS) for _ in range(n)])
print(f"{total / n:.2f}")


# Birthday Cake Candles
def birthdayCakeCandles(candles):
    max_height = max(candles)
    return candles.count(max_height)


# Number Line Jumps
def kangaroo(x1, v1, x2, v2):
    if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    return "NO"


# Viral Advertising
def viralAdvertising(n):
    shared = 5
    liked = 0
    cumulative = 0
    for _ in range(n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return cumulative


# Recursive Digit Sum
def superDigit(n, k):
    def sum_digits(s):
        if len(s) == 1:
            return int(s)
        return sum_digits(str(sum(int(char) for char in s)))
    
    initial_sum = sum_digits(n) * k
    return sum_digits(str(initial_sum))


# Insertion Sort - Part 1
def insertionSort1(n, arr):
    element = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] > element:
        arr[i + 1] = arr[i]
        print(*(arr))
        i -= 1
    arr[i + 1] = element
    print(*(arr))