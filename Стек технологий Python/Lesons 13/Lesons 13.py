
#Двумерные списки


# Простейшая аналогия - многоэтажный дом
# Двумерный список - это список содержащий списки
# например
        # tmp = [[1, 2, 3], [4, 5], [9, 8, 7]]

# есть этаж на котором квартиры [1, 2, 3] имеет индекс 0
# есть этаж на котором квартиры [4, 5] имеет индекс 1
# есть этаж на котором квартиры [9, 8, 7] имеет индекс 2

# Попробуем обратится к этажу на котором квартиры [4, 5]
        # print(tmp[1])
# Но что если мы хотим постучать в конкретную квартиру на этом этаже?
        # print(tmp[1][0])
# Давайте попробем изменить номер квартиры
# Сделать это можно точно так же как и в обычном списке, так как двумерный список все еще остается списком, и является изменяемым типом
        # tmp[1][0] = 9
        # print(tmp[1][0])
# Так же мы можем менять не только номер квартиры, но и целый этаж
        # tmp[1] = [4, 9, 0, 3]
        # print(tmp[1])
# С двумерными списками работают те же методы что и с обычными списками например метод append
# Допустим мы хоти добавить этаж нашему дому
        # tmp.append([6, 9, 2])
        # print(tmp)
# Вывод списка в более лаконичном виде
# Мы можем вывести каждый список(этаж) по очереди с помощью цикла for
        # for i in tmp:
        #     print(*i)
# Выводить научились, теперь научимся Вводить двумерные списки
# Например нам вводится два числа - количсетво внутренних списков и сами внутренние списки



# def pl(t):
#     for i in t:
#         print(*i)



            # n = int(input())
            # tmp = []
            # for i in range(n):
            #     a = list(map(int, input().split())) # теперь нужно ввести сам список квартир и добавить его в список tmp
            #     tmp.append(a)

            # pl(tmp)
# print(tmp)

# теперь сделаем функцию которая правильно выводит списки
# напоминание: каждая функция начинается с ключевого слова def и они должны находится перед кодом который ее использует
#====================================================================

# Мы научились вводить, выводить и задавать самым простым способом через перечисление списки

# def pl(t):
#     for i in t:
#         print(*i)

# tmp = [[1, 2], [3, 4]]

# А что если мы хотим создать двумерный список большо размера. например 5 на 5 руками это не самый классный способ

# Сначала зададим пустые списки tmp = [[] ]
# Теперь с помощью цикла мы пишем сколько раз мы хотим написать этот внутрений список внутри списка
                # tmp = [[] for i in range(5)]
# Мы создали список внутри которого лежит 5 пустых списков. Теперь заполним их.
# укажем что внутри будут лежать 1, и у каждого внутреннего элемента будет 7 жллементов

            # tmp = [[1 for i in range(7)] for i in range(5)]
# теперь выведем наш список
            # print(tmp)
# и пожалуй воспользуемся нашей функцией. не зря же делали ее
            # pl(tmp)
#===========================================================

# Практика:
# Задача: Сергей семенович сабянин поручил построить необыный домик, в котором будет Х этажей, и на каждом этаже Y квартир.
# Но вы не обыный архитектор, и решили вложить частичку своей души и следать так чтобы квартиры на каждом этаже нумировали в разные стороны
# на четных этажах справа налево, на нечетных слева на право. 
# таким образом на первом этаже самая левая квартира будет иметь номер 1
# а на втором самая правая будет иметь номер Y+1

def pl(t):
    for i in t:
        print(*i)

x= int(input())
y = int(input())

# house = [[] for i in range(x)] Сделали этажи
# house = [[0 for i in range(y)] for i in range(x)] Сделали этажи и квартиры
house = [[0 for i in range(y)] for i in range(x)] #Это "каркас" нашего дома
# Теперь нужно ввести номера квартир и показать наш дом
numb = 1 #номер очередной квартиры которую нумеруем. Начнем с 1, так как квартиры нумеруются с 1
# так как самый первый этаж находится наверху, мы используем отрицательную индексацию
for i in range(-1, -x -1, -1):
    # print(i) #Проверим что этажи идут в нужнои порядке
    # Теперь нам нужно пройтись по квартирам на каждом этаже
    if i % 2 == 1:
        for j in range(y):
            house[i][j] = numb #говорим что hous i этажа j квартиры будет равен numb(номеру квартиры)
            numb += 1 #увеличиваем номер квартиры на 1
    else:
        for j in range(-1, -y -1, -1): #идем от -1, до -у -1(так как не включительно -у) с шагом -1
            house[i][j] = numb #говорим что hous i этажа j квартиры будет равен numb(номеру квартиры)
            numb += 1 #увеличиваем номер квартиры на 1

pl(house)

# Списки могут иметь более одного уровня вложения 3, 4, 5 мерные
# например 3х мерный список

t3 = [[[1, 2], [ 3, 4]], [[5, 6], [ 7, 8]]]

# чтобы обротится к первому вложенному списку, скажем
print(t3[0])
# чтобы обротится к первому вложенному списку внутри первого вложеного списка, скажем
print(t3[0][0])
# чтобы обротится к первому элементу вложенному в первый список внутри первого списка, скажем
print(t3[0][0][0])