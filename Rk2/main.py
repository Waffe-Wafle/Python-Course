from Rk2_Classes import *
from os import system
from unittest import main

def word_in_orchestra_search(orchestras_list, conductors_list, orchestras_dict, word):
    for i in range(len(orchestras_list)):
        if word in orchestras_list[i].name:
            conductors_list.extend(orchestras_dict[i])
            yield orchestras_list[i]

def return_conductors(storage, conductors_list):
    for i in range(len(conductors_list)):
        yield storage.return_conductor_by_id(conductors_list[i])

def show_middle_salary_list(orcestra_list, average_salaries_list):
    for i in range(len(average_salaries_list)):
        orcestra_id = average_salaries_list[i][1]
        yield {"название": orcestra_list[orcestra_id].show(False),
              "id": "(id = " + str(orcestra_id) + ")",
              "срзп": average_salaries_list[i][0]
              }

def check_conductures_first_letter(conductors_list, orcestra_list, letter):
    for i in range(len(conductors_list)):
        if letter == (conductors_list[i].sername)[0]:
            orcestra_id = conductors_list[i].orchestra_id
            yield {"фио": conductors_list[i].show(False),
                   "id": "(id = " + str(conductors_list[i].conductor_id) + ")",
                   "оркестр": orcestra_list[orcestra_id].name,
                   "фамилия": conductors_list[i].sername
                   }

def main1():
    S = Storage()
    
    #Создаем оркестры:
    S.add_orchestra([Orchestra("Малый симфонический"), Orchestra("Практикантов (малый)"), Orchestra("Большой симфонический"), Orchestra("Очень малый малый")])
    new_orchestra = Orchestra("Не знаю, как назвать :<")
    S.add_orchestra([new_orchestra])
    
    #Создаем дирижеров:
    S.add_conductor([Conductor(0, "Иван",    "Крылов", "Матвеевич",  250000), Conductor(0, "Григорий", "Авдеев", "Артемович",    300000)],  0)
    S.add_conductor([Conductor(1, "Troll",   "Face",   "Memow",      15000),  Conductor(1, "V", "Анонимный",      "Anonimous",    1830000)], 1)
    S.add_conductor([Conductor(2, "Василий", "Шуткин", "Тотсамович", 257000), Conductor(2, "Товарищ",  "Майор",  "Вездесущевич", 100)],     2)
    S.add_conductor([Conductor(S.find_orcestra_by_name("Очень малый малый"), "Антон",     "Антонов",        "Михеевич",      248000)], 
                    S.find_orcestra_by_name("Очень малый малый"))
    S.add_conductor([Conductor(S.find_orcestra_by_name("Очень малый малый"), "Рептилоид", "Мировопорядков", "Иллюминатович", 248000)], 
                    S.find_orcestra_by_name("Не знаю, как назвать :<"))

    #================================[E1]================================#
    workers_list = [] #Лист дирижеров оркестров, удовлетворяющих требованию

    #Выведем все оркестры, в названия которых входит слово "малый"(c учетом регистра)
    print("Оркестры, содержащие в названии слово \"малый\" (с учетом регистра):")
    for i in word_in_orchestra_search(S.orchestras_list, workers_list, S.orchestras_dict, "малый"):
        i.show(); print("; ", end ="")

    #И всех дирижеров этих оркестров:
    print("\n\nДирижеры этих оркестров:")
    for i in return_conductors(S, workers_list):
            i.show(); print("; ", end="")

    #================================[E2]================================#
    #Рассчитаем среднюю зарплату и занесем во вложенный список:
    print("\n\n\nОркестры по возрастанию средней зарплаты в них:")
    average_salaries_list = S.count_average_salary()

    #Выведем его:
    for i in show_middle_salary_list(S.orchestras_list, average_salaries_list):
       print("%-26s%-9s%-3s%6d%7s" % (i["название"], i["id"], "->", i["срзп"], "рублей"))
    
    #================================[E3]================================#
    #Выведем список всех дирижеров, чья фамилия начинается на А и названия их отделов:
    print("\n\n\nСписок всех дирижеров, чья фамилия начинается на А и их названия оркестров:")
    for i in check_conductures_first_letter(S.conductors_list, S.orchestras_list, "А"):
        print("%-16s%-9s%-9s%6s" % (i["фио"], i["id"], "оркестр:", i["оркестр"]))

if __name__ == "__main__":
    #main1()
    #system("pause")
    main()
