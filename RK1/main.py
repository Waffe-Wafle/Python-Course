from Rk1_Classes import *

def main():
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

    #Выведем все оркестры, в названия которых входит слово "малый"(c учетом регистра):
    print("Оркестры, содержащие в названии слово \"малый\" (с учетом регистра):")
    for i in range(len(S.orcestra_list)):
        if "малый" in S.orcestra_list[i].name:
            S.orcestra_list[i].show(); print("; ", end ="")
            workers_list.extend(S.orchestra_dict[i])
    print("\n\nДирижеры этих оркестров:")

    #Выведем всех дирижеров этих оркестров:
    for i in range(len(workers_list)):
        (S.return_conductor_by_id(workers_list[i])).show(); print("; ", end="")

    #================================[E2]================================#
    #Рассчитаем среднюю зарплату и занесем во вложенный список:
    print("\n\n\nОркестры по возрастанию средней зарплаты в них:")
    average_salaries_list = S.count_average_salary()

    #Выведем его:R
    for i in range(len(average_salaries_list)):
        orcestra_id = average_salaries_list[i][1]
        print("%-26s%-9s%-3s%6d%7s" % (S.orcestra_list[orcestra_id].show(False), "(id = " + str(orcestra_id) + ")", "->", average_salaries_list[i][0], "рублей"))
    
    #================================[E3]================================#
    #Выведем список всех дирижеров, чья фамилия начинается на А и названия их отделов:
    print("\n\n\nСписок всех дирижеров, чья фамилия начинается на А и их названия оркестров:")
    for i in range(len(S.conductors_list)):
        if "А" in S.conductors_list[i].sername:
            orcestra_id = S.conductors_list[i].orchestra_id
            print("%-16s%-9s%-9s%6s" % (S.conductors_list[i].show(False), "(id = " + str(S.conductors_list[i].conductor_id) + ")", 
                                        "оркестр:", S.orcestra_list[orcestra_id].name))

if __name__ == "__main__":
    main()


