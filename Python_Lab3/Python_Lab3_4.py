#Сортировка по мудулю:
data = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]
import math


if __name__ == '__main__':
    print(sorted(data, key = abs, reverse = True), end ='\n\n')

    result_with_lambda = sorted(data, key = lambda x: abs(x), reverse = True)
    print(result_with_lambda)