""" 
Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада. Вклад составляет X рублей Y
копеек. Определите размер вклада через год. Программа получает на вход целые числа P,X,Y и должна вынести два числа:
величину вклада через год в рублях и копейках. Дробная часть копеек отбрасывается.
"""

#Вводим данные: Ставка - P, Рублики - Х и Копейки - Y
P = int(input ())
X = int(input ())
Y = int(input ())

#Считаем всё в копейках что бы всем было хорошо
Deposit = X * 100 + Y
Deposit_res = Deposit + Deposit * (P / 100)
X_res = int(Deposit_res / 100)
Y_res = int(Deposit_res) % 100

print(X_res)
print(Y_res)

