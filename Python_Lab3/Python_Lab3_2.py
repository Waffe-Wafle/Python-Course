#Выдача рандомного числа:
from random import randint
def random_generator(Number, A, B):
    for i in range(Number): yield randint(A, B)


#Проверка:
if __name__ == '__main__':
    G = random_generator(5, 1, 100)
    for i in G:
        print(i, end='; ')