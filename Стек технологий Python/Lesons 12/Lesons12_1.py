# Сортировка
# ПУЗЫРЬКОВАЯ
# a = [4, 9, 0, 17, 23, 4, 1, 0]
# n = len(a)

# for i in range(n):
#     for j in range(n-1-i):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
        
# print(*a)

# a[0], a[2] = a[2], a[0]
# print(a[0], a[2])

# c1 = 3
# c2 = 4
# c1, c2 = c2, c1
# print(c1, c2)

# def cmp(x):
#     return x % 10

# a = [4, 9, 0, 17, 23, 4, 1, 0]
# a.sort(key=cmp)
# print(a)
##################################################################
# Задача 1: 
# Есть количество сотрудников
# Есть зарплата каждого сотрудника
# Есть время работы каждого сотрудника
# отсортировать их по возрастанию зарплате
# n = 5
# sph = [12, 30, 97, 5, 6]
# hs = [10, 120, 4, 8, 9]

# res = []
# for i in range(n):
#     r = sph[i]* hs[i]
#     res.append(r)

# res.sort()
# print(res)
##################################################################
# Задача 2:
# Есть список чисел
# Отсортировать числа по произведениям первой цифры и второй цифры

# def kmp(x):
#     return (x//10) * (x%10)

# tmp = [12, 34, 35, 12, 19, 29]
# tmp.sort(key=kmp)
# print(tmp)
##################################################################
# a = 5
# b = 8
# c = 1
# d = -19

# print(max(a, b, c, d))
# print(min(a, b, c, d))
##################################################################
# tmp = [1, 4, -19, 30, 56]
# print(max(tmp))
# print(min(tmp))
##################################################################
# Кортежи не изменяемые списки
a = (2, 4, 9, 7)
