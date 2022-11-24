#Напишите программу, которая принимает на вход координаты точки
#(X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
#(или на какой оси она находится).
#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3



x = float(input('Введите значение х: '))
y = float(input('Введите значение y: '))

if x > 0 and y > 0:
    print('Четверть №1')
elif x > 0 and y < 0:
    print('Четверть №4')
elif x < 0 and y < 0:
    print('Четверть №3')
elif x < 0 and y > 0:
    print('Четверть №2')
else:
    print('Ошибка')