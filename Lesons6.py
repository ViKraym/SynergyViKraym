# Задание №1
# Сначала вводится число N затем вводится ровно N целых чисел. Подсчитайте, сколько из них равны нулю, и выведите это количество.

N = int(input())
itter = 1
number = 0
CountN = 0

while itter <= N:
    number = int(input())
    itter += 1
    if number == 0:
        CountN += 1 

print("Количество чисел равных нулю: ", CountN)
    
# Задание №2
# Вводится натуральное число X. Подсчитайте количество натуральных делителей числа X (включая 1 и само число). x ≤ 2e9 (2 миллиарда)

X = int(input())
cntDel = 0

if X==1:
    d = 1
else:
    d = 2
    for i in range(2, int((X/2)+1)):
        if X%i == 0:
            d += 1

print(d)

# Задание №3
# Вводятся целые числа A и B. Гарантируется, что A ≤ B. Выведите все четные числа на заданном отрезке через пробел.

A = int(input())
B = int(input())

for i in range(A, B):
    if i%2 == 0:
        print(i)