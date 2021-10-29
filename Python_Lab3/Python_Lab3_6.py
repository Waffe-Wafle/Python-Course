#Расчет времени исполнения:
from contextlib import contextmanager
from time import time; from time import sleep


#Для нормального человеческого округления:
def normal_people_round(number, ndigits=0):
    ndigits += 1
    n = round(number, ndigits)*(10**ndigits)
    m = n % 10
    n -= m
    if m >= 5:
        n += 10
    n /= (10**ndigits)
    return n


#С использованием библиотеки:
@contextmanager
def time_counter(ndigits):
    try:
        time_start = time()
        yield
    except:
        print("We had an error!")
    finally:
        time_end = time()
        proces_time = time_end - time_start
        print('Затрачено: ', normal_people_round(proces_time, ndigits), ' c')
        

#С использованием класса:
class Timer():
    def __init__(self, ndigits):
        self.time_start = 0
        self.ndigits = ndigits

    def __enter__(self):
        self.time_start = time()
 
    def __exit__(self, exc_type, exc_value, exc_traceback):
        proces_time = time() - self.time_start
        print('\nЗатрачено: ', normal_people_round(proces_time, self.ndigits), ' c')
  
 

def test(n=5):
        times = 0
        while True:
            print("f")
            times += 1
            if times > n:
                break
   
            
if __name__ == "__main__":
    with time_counter(8):
       sleep(1.5)

    with Timer(8):
        sleep(1.5)
