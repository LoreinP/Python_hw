from math import ceil


def square(a):
    s = a ** 2
    return s


a = float(input("Длина стороны квадрата: "))
print(f'Округленная в большую сторону сумма - {square(a)}')




