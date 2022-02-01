# Task 06.
# 
# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
#

def fn_upperCaseFirst(pn_word):
    return pn_word[0].upper() + pn_word[1:]

vs_word = input("Enter the word in lower case: ")
print(fn_upperCaseFirst(vs_word))
