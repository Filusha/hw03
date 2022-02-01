# Task 01.
# 
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
#
def fn_quotient(pf_divident, pf_divisor):
    if pf_divisor == 0:
        print("divisor cannot be 0.")
        return False
    else:
        return ( pf_divident / pf_divisor )

vf_dividend = float(input("Input dividend: "))
vf_divisor = float(input("Input divisor: "))
vv_result = fn_quotient(vf_dividend, vf_divisor)
print("Calculation result: ", vv_result)




