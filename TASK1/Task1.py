'''Вычислить число c заданной точностью d
Пример:
при d = 0.001, π = 3.141
10^(-1) ≤ d ≤10^(-10)'''

from math import pi

d =  int(input("Введите любое целое число:"))
print(f'число Pi для введенного числа с заданной точностью равно {round(pi, d)}')