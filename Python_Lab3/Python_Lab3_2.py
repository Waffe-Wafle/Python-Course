from random import randint
def random_generator(Number, A, B):
    for i in range(Number): yield randint(A, B)

#Проверка:
if __name__ == '__main__':
    G = random_generator(30, 1, 20)
    for i in G:
        print(i, end='; ')