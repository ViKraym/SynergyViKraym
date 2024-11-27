
# Задание №1

# В первой строке вводится число N. Далее в N строк вводится N чисел (1 ≤ N ≤ 10000), по одному числу на строке. 
# Все числа по модулю не превышают 10e5. Переверните массив чисел. Выведите N чисел - перевернутый массив.
print("Задание №1")
print("Введте количество строк:")
N = int(input())
print("Введте числа:")
res = []

for j in range(N):
    a = int(input())
    if a >= 1 and a <= 10000:
        res.append(a)

res.reverse()
print(*res)


# Задание №2

# В первую строчку вводится число B (1 ≤ B ≤ 100 000). В следующую строку через пробел вводятся B чисел (1 ≤ Ai ≤ 10e9). Вам требуется написать метод, который получает на вход массив и изменяет его таким образом, чтобы на первом месте стоял последний элемент, на втором - первый, на третьем - второй и т. д. Выведите N чисел - измененный массив.
print("Задание №2")
print("Введте количество чисел:")
B = int(input())
print("Введте числа через пробел:")
res1 = list(map(int, input().split()))
res1.insert(0, res1.pop()) # В ячейку с индексом 0 мы вставляем (.insert) значение удаленное(.pop) методом 

print(*res1)

    
# Задание №3

# На берегу реки стояли n рыбаков, все они хотели перебраться на другой берег. Одна лодка может выдержать не более m килограмм, при этом в лодку помещается не более 2 человек. 
# Определите, какое минимальное число лодок нужно, чтобы перевезти на другой берег всех рыбаков В первую строку вводится число m (1 ≤ m ≤ 10e6) - максимальная масса, которую может выдержать одна лодка. 
# Во вторую строку вводится число n (1 ≤ n ≤ 100) - количество рыбаков. В следующие N строк вводится по одному числу Ai (1 ≤ Ai ≤ m) - вес каждого путешественника. 
# Программа должна вывести одно число - минимальное количество лодок, необходимое для переправки всех рыбаков на противоположный берег.
# если сумма масс двух рыбаков не привышает максимальной грузоподемности лодки, то мы добавляем 1 иначе 2

print("Задание №3")
print("Сколько выдержит лодка?")
m = int(input())
if 1 <= m <= 10e6:
    print(" соответсвие условию")
else:
     print("не соответсвие условию")

print("Сколько рыбаков?")
n = int(input())
if 1 <= n <= 100:
    print("соответсвие условию")
else:
     print("не соответсвие условию")

res2 = []


while len(res2) < n:
    a = int(input())
    if 1 <= a <= m:
        res2.append(a)

res2.sort()
min = 0
max = n - 1
cnt = 0

while min <= max:
    sum = res2[min] + res2[max]
    if res2[min] == res2[max]:
        min += 1
    elif sum <= m:
        min += 1
        max -= 1
    else:
        max -= 1
    cnt += 1 
          
print(cnt)





    
