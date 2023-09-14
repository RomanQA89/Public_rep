''' Функция, которая принимает список с числами my_list и строку string.
Функция должна вернуть тот же список,
отсортированный в зависимости от значения string.
Если строка "Asc" (от англ. ascending), список нужно отсортировать в порядке возрастания.
Если строка "Des" (от англ. descending), список нужно отсортировать в порядке убывания.
Если строка "None", функция должна вернуть список без изменений.'''

my_list = list(map(int, input('Введите числа через пробел: ').split()))
string = input('Введите любую строку: ')

def NumStr(my_list):
    if string == 'Asc':
        my_list.sort()
        return f"Список по возрастанию: {my_list}"
    elif string == 'Des':
        my_list.sort(reverse=True)
        return f"Список по убыванию: {my_list}"
    elif string == 'None':
        return f"Неотсортированный список: {my_list}"

print(NumStr(my_list))