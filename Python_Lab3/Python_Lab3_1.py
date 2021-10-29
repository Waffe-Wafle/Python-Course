#Последовательная выдача ключей из словаря:
elements = [
    {'title': None, 'color': 'red', 'title': 'ololo'},
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]


def fild_generator(list, *args):
    #Если аргументов несколько:
    if len(args) > 1:
        #Для каждого словаря:
        for i0 in list:
            result = {}
            #Поиск ключа аналогичного аргументу c не None значением:
            for i1 in args:
                value = i0.get(i1, None)
                if value != None: result[i1] = value
            if result != {}: yield result
    #Если аргумент 1
    elif len(args) > 0:
         for i0 in list:
             value = i0.get(args[0], None)
             if value != None: yield value
    else: raise Exception('No arguments in fild_generator!')
    

#Проверка:
if __name__ == '__main__':
    f = fild_generator(elements, 'title', 'price', 'color')
    for i in f:
        print(i)
    print('\n\n')
    f = fild_generator(elements, 'title')
    for i in f:
        print(i)
