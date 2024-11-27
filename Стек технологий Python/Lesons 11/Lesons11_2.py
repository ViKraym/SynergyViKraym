
# def get_suffix(age_pit):

    

   
    
    

def create():
    
        print("Укажите имя питомца:")
        name1 = input()
        name = name1.lower()
        card[name] = dict()

        print("Вид питомца:")
        tip_pit = input()
        card[name]["вид"] = tip_pit.lower()

        
        print("Возраст вашего питомца:")
        
        age_pit = int(input())
       

        if (age_pit % 10 == 1) and (age_pit != 11) and (age_pit % 100 != 11):
                age_pit = str(age_pit) + ' год'

        elif (1 < age_pit % 10 <= 4) and (age_pit != 12) and (age_pit != 13) and (age_pit != 14):
            age_pit = str(age_pit) + ' года'  
            
        else:
            age_pit = str(age_pit) + ' лет'

        card[name]["Возраст"] = age_pit
        

        print("Имя владельца питомца:")
        owner_pit = input()
        card[name]["хозяин"] = owner_pit.lower()
       
        print("\n""Карточка питомца успешно добавлен в Базу данных")

def read():
    print("Назовите имя питомца, карту которого вы хотите посомотреть")
    name1 = input()
    name = name1.lower()
    if name in card:
        print("\n""Это", card[name]['вид'], "по кличке", "'{}'".format(name), "Возраст питомца: ", card[name]['Возраст'], "Владельца зовут: ", card[name]['хозяин'])
    else:
        print("\n""Простите, но карточки такого питомца нет в нашей Базе")

def update():
    print("Назовите имя питомца, карту которого вы хотите отредактивровать?")
    name1 = input()
    name = name1.lower() 
    if name in card:
        print("\n""Что вы хотите изменить?")
        print("\n""Имя питомца")
        print("\n""Вид питомца")
        print("\n""Возраст питомца")
        print("\n""Имя хозяина")
        
    else:
        print("\n""Простите, но такого питомца нет")

def delete():
    print("Назовите имя питомца, карту которого вы хотите отредактивровать?")
    name1 = input()
    name = name1.lower()
    if name in card:
        print("\n""Карта питомца успешно удалена из Базы")
        card.pop(name)
    else:
        print("\n""Простите, но карточки такого питомца нет в нашей Базе")

card = dict()

print("Добро пожаловать в клинику.")
command = 0 

while command != 'stop':
    print('\n'"Выберете действие для продолжения""\n")
    print("1 - Создать новую запись о питомце")
    print("2 - Посмотреть карточку питомца")
    print("3 - Изменить существующую запись/внести корректировки")
    print("4 - Удалить запись о питомце")
    print("Чтобы закончить работу с Базой данных - Введите stop")

    command = input()
    command.lower()
      
    if command == "1":
        create()
    elif command == "2":
        read()
    elif command == "3":
        update   
    elif command == "4":
        delete()
  