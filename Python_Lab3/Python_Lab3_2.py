#Выдача рандомного числа:
from random import randint
from os import system
def random_generator(Number, A, B):
    for i in range(Number): yield randint(A, B)


#Проверка:
if __name__ == '__main__':
    G = random_generator(20, 1, 100)
    for i in G:
        print(i, end = '; ')
    system('pause')