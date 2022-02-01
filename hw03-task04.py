# Task 04.
# 
# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y.
# Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной
# функции возведения числа в степень.
#
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
# 

def fn_exponentiation1(pn_number, pn_power):
    vn_result = pn_number ** pn_power

    return vn_result

def fn_exponentiation2(pn_number, pn_power):
    if pn_power < 0:
        vb_power_negative = True
    else:
        vb_power_negative = False

    pn_power = abs(pn_power)
    vn_result = pn_number
    for I in range(pn_power - 1):
        vn_result = vn_result * pn_number

    if vb_power_negative:
        vn_result = 1 / vn_result

    return vn_result

vn_number = int(input("Input number: "))
vn_power = int(input("Input power: "))

vv_result = fn_exponentiation1(vn_number, vn_power)
print("Calculation result (using **): ", vv_result)

vv_result = fn_exponentiation2(vn_number, vn_power)
print("Calculation result (using a loop): ", vv_result)
