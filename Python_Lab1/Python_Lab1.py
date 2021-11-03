import sys
import os
import math
import msvcrt

#Получение коэффициента:
def Get_Coeficient(Prompt):
    while(True):
        try:
            print(Prompt, end = " ")
            Coef_Str = input()
            Coef = float(Coef_Str) #Переводим строку в действительное число
            return Coef
        except: pass               #При невозможности преобразовать в число перезапрос

#Непосредственные расчеты:
def Get_Result(A, B, C):
    D = B*B - 4*A*C
    Result = []
    if D >= 0:
        Sqrt = math.sqrt(D)
        Root1 =  (Sqrt - B) / (2.0 * A)
        Root2 = (-Sqrt - B) / (2.0 * A)
        if Root1 == Root2:
            Result.append(Root1)
        else:
            Result.append(Root1)
            Result.append(Root2)
        return Result
    else:
        return None

#Главная функция:
def Main():
    while (True):
        Arg_List = []
        print("Программа для решения квадратного уравнения (вид Ax^2+Bx+C)")
        Arg_List.append(Get_Coeficient("Введите коеффициент A квадратного уравнения:"))
        Arg_List.append(Get_Coeficient("Введите коеффициент B квадратного уравнения:"))
        Arg_List.append(Get_Coeficient("Введите коеффициент C квадратного уравнения:"))
        Result = Get_Result(*Arg_List)
        Result_Str = "│Для (" + str(Arg_List[0]) + ")x^2 + (" + str(Arg_List[1]) + ")x + (" + str(Arg_List[2]) + ")" 
        if Result != None:
            if len(Result) == 2:
                Result_Str += " были получены корни: "
            else:
                Result_Str += " был получен корень: "
        else:
            Result_Str += " корней - "
        Result_Str += str(Result).strip("[]").replace(",", " и") + "│"
        print("\n┌", end = "")
        for I in range(len(Result_Str)-2): print("─", end = "")
        print("┐", end = ""); print("\n" + Result_Str); print("└", end = "")
        for I in range(len(Result_Str)-2): print("─", end = "")
        print("┘", end = "")

        #При необходимости повторить операцию:
        print("\nПовторить операцию/Выйти: Enter/Пробел?")
        if str(msvcrt.getch()) == "b' '": return
        os.system("cls")

if __name__ == "__main__":
    Main()