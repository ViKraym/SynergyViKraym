
# Задание №1

# На вход подается 1 строка без пробелов. По данной строке определите, является ли она палиндромом (то есть, можно ли прочесть ее наоборот, как, например, слово "шалаш"). Необходимо вывести ”yes”, если строка является палиндромом, и “no” в противном случае.

string = input()

if string[::1] == string[::-1]:
    print ("Yes")
else:
    print ("No")

# Задание №2
# Дана строка, длина которой не превосходит 1000. Вам требуется преобразовать все идущие подряд пробелы в один. Выведите измененную строку.

string = input().split()

if len(string) <= 1000: 
    string_res = ""
    for i in string:
        string_res += i+" "
    print(string_res)
else:
    print("Введенная строка длинее 1000 символов")