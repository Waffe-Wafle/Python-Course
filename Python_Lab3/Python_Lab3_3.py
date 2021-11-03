#Пропуск дубликатов:
import inspect
from os import system
class Unique:
    def __init__(self, Item, **kwargs):
        if type(Item) != list and inspect.isgenerator(Item) == False: 
            raise Error('Некорректный тип аргумента итератора! ('+ str(type(Item)) + ', а требуются: list/generator)')
        if type(Item) == list: self.arg_list = True
        else:                  self.arg_list = False

        self.ignore_case = kwargs.get('ignor_case', None)
        if self.ignore_case == None: self.ignore_case = False
        self.elements_list = []
        self.item = Item
        self.i = 0


    def __next__(self):
        #Если на входе имеется лист:
        if self.arg_list == True: 
            if len(self.item) <= self.i: raise StopIteration
            Got_item = self.item[self.i]
            self.i+=1
        #Если использовался генератор:
        else:
            try: Got_item = next(self.item)
            except: raise StopIteration
        
        if Got_item in self.elements_list: return
        elif not self.ignore_case:#
            self.elements_list.append(Got_item)
            return Got_item
        elif type(Got_item) == str:
            found = False
            for i2 in self.elements_list:
                if Got_item.upper() == i2 or Got_item.lower() == i2: 
                    found = True; break
            if not found: 
                self.elements_list.append(Got_item)
                return Got_item
        else:  
            self.elements_list.append(Got_item)
            return Got_item


    def __iter__(self):
        return self


#Проверка:
if __name__ == '__main__':
    from Python_Lab3_2 import random_generator
    listik = [1, 2, 3, 'HI', 'hi', 'some_text', 'А', 'а']
    G = random_generator(10,1,5) 
    d1 = Unique(G, ignor_case = True)
    d2 = Unique(listik, ignor_case = True)
    for i in d1:
        print(i)
    print('\n\n')
    for i in d2:
        print(i)
    system('pause')