#Класс дирижера:
class Conductor:
    conductors_number = 0 #Счетчик для id
    def __init__(self, Orchestra_id=None, Name="", Sername="", Middle_name="", Salary=None, Orchestra_name=""):
        self.conductor_id = Conductor.conductors_number
        Conductor.conductors_number+=1
        self.orchestra_id = Orchestra_id
        self.name         = Name
        self.sername      = Sername
        self.middle_name  = Middle_name
        self.salary       = Salary

    #Краткий вывод экземпляра:
    def show(self, Logic=True):
        line = self.name + " " + self.sername
        if Logic == True: print(line + " (id = " + str(self.conductor_id) + ", оркестр_id = " + str(self.orchestra_id) + ")", end="")
        return line

#Класс оркестра:
class Orchestra:
    orchestras_number = 0 #Счетчик для id
    def __init__(self, Name=""):
        self.orchestra_id = Orchestra.orchestras_number
        Orchestra.orchestras_number+=1
        self.name = Name
    
    #Краткий вывод экземпляра:
    def show(self, Logic=True):
        line = "\"" +self.name + "\""
        if Logic == True: print(line + " (id = " + str(self.orchestra_id) + ")", end="")
        return line

#Класс дирижеров оркестров (для реализации связей и хранения данных):
class Storage:
    orchestra_dict  = {} #Словарь относительно оркестров
    orcestra_list   = [] #Cписки оркестров и дирижеров
    conductors_list = [] #

    #Добавление новых дирижеров:
    def add_conductor(self, Conductors, Orchestra_id):
        conductors_of_orchestra = Storage.orchestra_dict.get(Orchestra_id, None) #Поиск соответсвующего оркестра
        if conductors_of_orchestra != None: 
            if isinstance(Conductors, list) == True: #Если такой имеется и соблюден синтаксис добавляем необходимых дирижеров
                for i in range(len(Conductors)): conductors_of_orchestra.append(Conductors[i].conductor_id) #в лист связей
                Storage.conductors_list.extend(Conductors)                                                  #в хранилище дирижеров
            else: print("Ошибка синтаксиса!")
        else: print("Отсутсвует данный оркестр!")

    #Добавление новых оркестров:
    def add_orchestra(self, Orchestras):
        if isinstance(Orchestras, list) == True:
            for i in range(len(Orchestras)): self.orchestra_dict[Orchestras[i].orchestra_id] = [] #в лист связей
            Storage.orcestra_list.extend(Orchestras)                                              #в хранилище оркестров
        else: print("Ошибка синтаксиса!")
    
    #Возвращение дирижера по id:
    def return_conductor_by_id(self, Conductor_id): 
        try: return Storage.conductors_list[Conductor_id]
        except: return None

    #Возвращение id оркестра по его имени:
    def find_orcestra_by_name(Storage, Name):
        for i in range(len(Storage.orcestra_list)):
            if Storage.orcestra_list[i].name == Name: return i
        return None

    #Cоздание отсортированного по возрастанию списка средних зарплат в оркестрах:
    def count_average_salary(self):
        sallary_range_list = []
        for i in range(len(Storage.orchestra_dict)):
            summ = 0;
            for i2 in range(len(Storage.orchestra_dict[i])): 
                summ += Storage.conductors_list[Storage.orchestra_dict[i][i2]].salary #Сумма месячных зарплат в этом оркестре
            Average = round(summ/len(Storage.orchestra_dict[i]), 2)                   #Находим среднее
            sallary_range_list.append([Average, i])                                   #Добавляем его соответсвенно с id оркестра
        sallary_range_list.sort()
        return sallary_range_list