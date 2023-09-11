import random

array = list(map(int, input('Введите любое количество целых чисел через пробел: ').split()))

# Функция быстрой сортировки.
def qsort(array, left, right):
    p = random.choice(array[left:right + 1])          # Рандомный контрольный элемент для сравнения с левой и правой частью.
    i, j = left, right                                # Индексы левой и правой части.
    while i <= j:                                     # Пока индексы левой части не превысили индексы в правой
        while array[i] < p:                           # Пока элементы в левой части меньше контрольного(среднего) элемента
            i += 1                                    # Проходимся по всем левым элементам пока они соответствуют предусловию.
        while array[j] > p:                           # Пока элементы в правой части больше контрольного(среднего) элемента
            j -= 1                                    # Проходимся по всем правым элементам пока они соответствуют предусловию.
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
    return array

# Функция двоичного поиска.
def binary_search(array, number, left, right):
    if left > right:                                             # если левая граница превысила правую, т.е. индекс крайнего левого элемента больше всех остальных.
        return False                                             # значит элемент отсутствует
    elif number == array[0]:                                     # индекс элемента невозможно установить, т.к. вводимое пользователем число является левой границей диапазона.
        return False
    middle = (right + left) // 2                                 # находим середину
    if array[middle] == number:                                  # если элемент в середине,
        if array[middle - 1] < number <= array[middle]:
            return middle - 1                                    # возвращаем этот индекс
    elif number < array[middle]:                                 # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, number, left, middle - 1)
    else:                                                        # иначе в правой
        return binary_search(array, number, middle + 1, right)

# Цикл будет срабатывать до тех пор, пока пользователь не введет верное значение.
while type:
    number = input('Введите любое целое число из списка: ')
    try:
        number = int(number)
    except ValueError:
        print(f'"{number}" не является целым числом')
    else:
        print(f"Отсортированная матрица: {qsort(array, 0, len(array) - 1)}")
        print(f"Индекс установленного элемента: {binary_search(array, number, 0, len(array) - 1)}")

        if number < array[0] or number > array[-1]:
            print('Числа нет в диапазоне')
        elif number == array[0]:
            print('Индекс элемента невозможно установить, т.к. он выходит за пределы диапазона.')
        break