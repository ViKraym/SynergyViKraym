# Задание №1

# В первую строку вводится число N – количество чисел (1 ≤ N ≤ 100000). 
# Во вторую строку вводится через пробел N чисел, каждое не превышает 2*10e9 по модулю. 
# Требуется выяснить, сколько среди этих чисел различных. 
# Выведите число, равное количеству различных чисел среди данных.


print("Введите количество чисел")
N = int(input())
if 1 <= N <= 100000:
    print("соответсвие условию")
else:
    print("не соответсвие условию")


res =  list(map(int, input().split()))
res1 = []
for j in range(len(res)):
    if  len(res) <= N :
       if 1 <= res[j] <= 100000:
           res1.append(res[j])
    else:
        print(f'Вы ввели больше {N} чисел' )
        break

res_s = set(res1)

print(len(res_s.union()))

# Задание №2

# Вводятся два списка чисел, которые могут содержать до 100000 чисел каждый. 
# Все числа каждого списка находятся на отдельной строке. 
# Выведите, сколько чисел содержится одновременно как в первом списке, так и во втором.

print("Введите количество чисел в первом списке")
c1 = int(input())
cl1 = []
for i in range(c1):
    print(f"Введите {i+1} число ")
    a = input()
    cl1.append(a)
uc1 = set(cl1)    

print("Введите количество чисел во втором списке")
c2 = int(input())
cl2 = []
for j in range(c2):
    print(f"Введите {j+1} число ")
    b = input()
    cl2.append(b)
uc2 = set(cl2)   

print(uc1.union(uc2))
print(len(uc1.union(uc2)))

# Задание №3

# Во входную строку водится последовательность чисел через пробел. 
# Для каждого числа выведите слово ”YES” (в отдельной строке), 
# если это число ранее встречалось в последовательности или ”NO”, если не встречалось.


print("Введите числа в строку")
numb = [int(s) for s in input().split()]
cur1 = set()
for i in numb:
    if i in cur1:
        print("YES")
    else:
        print("NO")
cur1.add(i)