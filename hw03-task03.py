# Task 03.
# 
# Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму
# наибольших двух аргументов.
#
def fn_sum_largest(pn_first, pn_second, pn_third):
    vl_numbers = [pn_first, pn_second, pn_third]
    vl_numbers.sort()
    return vl_numbers[1] + vl_numbers[2]

vn_result = fn_sum_largest(7, 45, 16)
print("Sum of the two largest arguments: ", vn_result)

