#Декоратор вывода:
def print_result(function):
    def wrapper(x):
        print('Исполняется: ' + str(function.__name__) + '\n')
        result = function(x)
        if isinstance(result, list): 
            for i in result: print(i)
        elif isinstance(result, dict):
            res_touple = result.fromkeys
            for i in result: print(res_touple[0] + ' = ' + res_touple[1])
        else: print(result)
        return result
    return wrapper


def Test(x):
    print('Идет исполнение Test')
    return x


#Проверка:
if __name__ == '__main__':
   test = print_result(Test)
   A = test(10)
   print('\n', A)
   