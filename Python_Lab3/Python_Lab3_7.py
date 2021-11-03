#Основное задание:
import json
import sys
from os import system
from Python_Lab3_5 import print_result
from Python_Lab3_3 import Unique
from Python_Lab3_6 import Timer
from Python_Lab3_2 import random_generator
path = 'Data.json'


with open(path, encoding='utf-8') as f:
    data = json.load(f)


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
        result.append(zip([i], ['зарплата: ' + str(list(random_generator(1, 100000, 200000))).strip('[]')]))
    return result


if __name__ == '__main__':
    with Timer(8):
        f4(f3(f2(f1(data))))
    system('pause')