#Основное задание:
import json
import sys
from Python_Lab3_5 import print_result
from Python_Lab3_3 import Unique
from Python_Lab3_6 import Timer
from Python_Lab3_2 import random_generator
path = 'Data.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария
with open(path, encoding='utf-8') as f:
    data = json.load(f)
# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

def f1(arg):
    return [i.capitalize() for i in Unique(arg, ignor_case = True) if i != None]


def f2(arg):
    return list(filter(lambda x: "Программист" in x or "программист" in x, arg))


def f3(arg):
    return [i + ' c опытом Python' for i in arg]

@print_result
def f4(arg):
    result = []
    for i in arg:
        result.append(i + ' , зарплата: ' + str(list(random_generator(1, 100000, 200000))).strip('[]'))
    return result


if __name__ == '__main__':
    with Timer(3):
        f4(f3(f2(f1(data))))