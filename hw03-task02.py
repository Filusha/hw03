# Task 02.
# 
# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе
# одной строкой.
#

def fn_data_processing(ps_name, ps_surname, pd_birthday, ps_city, ps_email, ps_phone):
    return ps_name + " " + ps_surname + ", " + pd_birthday + ", " + ps_city + ", " + ps_email + ", " + ps_phone



vs_ClientInfo = fn_data_processing(ps_name="Василий", ps_surname="Пупыркин", pd_birthday="01.01.1991", ps_city="Миндюкино", ps_email="VPupirkin@GMail.com", ps_phone="+7(999)111-2233")
print("Client information: ", vs_ClientInfo)