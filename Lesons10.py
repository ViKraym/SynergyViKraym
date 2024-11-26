# Bank = dict()
# n= int(input())

# for i in range(n):
#     req = input()
#     if req == "create":
#         k = input()
#         Bank[k] = 0
#     elif req == "add":
#         k = input()
#         amount = int(input())
#         if k in bank.keys():
#             Bank[k] += amount
#         else:
#             print("sorry, no such key")
#     else:
#             print("sorry, bad request")
# print(Bank)

# tmp = {"k1": 1, "k2": 10, "qwert": 5}
# bank = dict()
# print(tmp.keys())
# print(tmp.values())
# print(tmp.items())
# tmp.pop('k1')

# for k in tmp.keys():
#     print(k)


# company = {
#     "pits": {
#         "Alice": {"age": 25, "role": "Sales Executive"},
#         "Bob": {"age": 30, "role": "Sales Manager"}
#     },
   
# }

company = dict()
    
while True:
    print("Добро пожаловать в клинику. Какой у вас вопрос?")
    print("1 - Записать питомца")
    print("2 - Посмотреть анкету питомца")
    print("0 - Забрать питомца")

    req = input()
    if req == "1":
        print("Как зовут вашего питомца?")
        name = input()
        company[name] = dict()

        print("Вид вашего питомца:")
        tip_pit = input()
        company[name]["вид"] = tip_pit

        print("Возраст вашего питомца:")
        age_pit = int(input())
        company[name]["Возраст"] = age_pit
        if (age_pit == 1) or (age_pit == 21):
            ageUpd = str(age_pit) + " год."
        elif (5 > age_pit > 1) or (25 > age_pit > 21) or (35 > age_pit > 31):
            ageUpd = str(age_pit) + " года."
        elif (21 > age_pit > 4) or (24 < age_pit < 31):
            ageUpd = str(age_pit) + " лет."
        elif (35 < age_pit < 1):
            print("Ваш питомец либо еще не родился либо уже слишком стар. Извините.")
            break
        company[name]["Возраст"] = ageUpd
        print("Имя владельца питомца:")
        owner_pit = input()
        company[name]["хозяин"] = owner_pit
        
    
    elif req == "2":
        print("Как зовут вашего питомца?")
        name = input()
        print("Это",company[name]['вид'], "по кличке", '"{}".'.format(name), "Возраст питомца: ", company[name]['Возраст'], "Владельца зовут: ", company[name]['хозяин'] )
    

    elif req == "0":
        print("Как зовут вашего питомца?")
        name = input()
        if name in company:
            print("Вот ваш питомец")
            company.pop(name)
        else:
            print("Простите, но такого питомца нет")

        



# Задание 2


# degree = {}

# for i in range(10, -5-1, -1):
#     degree[i] = i**i
    
# print(degree)