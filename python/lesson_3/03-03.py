# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
#


def sum_two_max(x, y, z):
    """
    Функция принимает 3 числовых аргумента,
    удаляет из списка минимальный,
    и возвращает сумму оставшихся
    :param x:
    :param y:
    :param z:
    :return:
    """
    my_list = [x, y, z]
    my_list.remove(min(my_list))
    return sum(my_list)


print(sum_two_max(3, 4, 3))
