# def create():

# def read():

# def update():

# def delete():

card = dict()


print("Добро пожаловать в клинику.")


while True:
    print("Выберете действие для продолжения""\n")
    print("1 - Создать новую запись о питомце")
    print("2 - Посмотреть карточку питомца")
    print("3 - Изменить существующую запись/внести корректировки")
    print("4 - Удалить запись о питомце")

    command = input()
    
    if command == "1":
        print("Укажите имя питомца:")
        name = input()
        card[name] = dict()

        print("Вид питомца:")
        tip_pit = input()
        tip_pit
        card[name]["вид"] = tip_pit

        print("Возраст вашего питомца:")
        age_pit = int(input())
        
        if (age_pit % 10 == 1) and (age_pit != 11) and (age_pit % 100 != 11):
            year_case = str(age_pit) + ' год'

        elif (1 < age_pit % 10 <= 4) and (age_pit != 12) and (age_pit != 13) and (age_pit != 14):
            year_case = str(age_pit) + ' года'  
            
        else:
            year_case = str(age_pit) + ' лет'
        
        card[name]["Возраст"] = year_case

        print("Имя владельца питомца:")
        owner_pit = input()
        
        card[name]["хозяин"] = owner_pit
       
        print("\n""Карточка питомца успешно добавлен в Базу данных")

    elif command == "2":
        print("Назовите имя питомца, карту которого вы хотите посомотреть")
        name = input()
        
        if name in card:
            print("\n""Это", card[name]['вид'], "по кличке", "'{}'".format(name), "Возраст питомца: ", card[name]['Возраст'], "Владельца зовут: ", card[name]['хозяин'])
        else:
            print("\n""Простите, но карточки такого питомца нет в нашей Базе")

    elif command == "3":
            print("Назовите имя питомца, карту которого вы хотите отредактивровать?")
            name = input()
            
            if name in card:
                print("\n""Вот ваш питомец")
                card.pop(name)
            else:
                print("\n""Простите, но такого питомца нет")    

    elif command == "4":
        print("Назовите имя питомца, карту которого вы хотите отредактивровать?")
        name = input()
        if name in card:
            print("\n""Карта питомца успешно удалена из Базы")
            card.pop(name)
        else:
            print("\n""Простите, но карточки такого питомца нет в нашей Базе")