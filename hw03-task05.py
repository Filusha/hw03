# Task 05.
# 
# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.
#
vn_sum = 0
vb_quit = False
while True:
    vs_num_list = input("Enter few numbers separated by spaces, or exit <q>: ").lower()
    vn_pos_char = vs_num_list.find("q")
    if vn_pos_char > 0:
        vs_num_list = vs_num_list[:vn_pos_char - 1]
        vb_quit = True

    vl_num_list = vs_num_list.split(" ")
    for I in vl_num_list:
        vn_sum = vn_sum + int(I)

    print("Current summa: ", vn_sum)
    if vb_quit:
        break

