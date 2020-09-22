# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
#
item_name = input('Введите название товара (ВВОД, если закончить): ')
i = 1
items = []
while item_name != '':
    item_price = float(input('Введите стоимость товара: '))
    item_count = int(input('Введите кол-во товара: '))
    item_unit = input('Введите единицу измерения товара: ')
    items.append((i, {'название': item_name, 'цена': item_price, 'количество': item_count, 'ед': item_unit}))
    i += 1
    item_name = input('Введите название товара (ВВОД, если закончить): ')
#
# Пример данных
# items = [(1, {'название': 'компьютер', 'цена': 20000.0, 'количество': 5, 'ед': 'шт'}), (2, {'название': 'принтер', 'цена': 6000.0, 'количество': 2, 'ед': 'шт'}), (3, {'название': 'сканер', 'цена': 2000.0, 'количество': 7, 'ед': 'шт'})]
#
analytics = {'название': set(), 'цена': set(), 'количество': set(), 'ед': set()}
# выводим список товаров и заполняем словарь аналитики
for item in items:
    print(item)
    analytics['название'].add(item[1].get('название'))
    analytics['цена'].add(item[1].get('цена'))
    analytics['количество'].add(item[1].get('количество'))
    analytics['ед'].add(item[1].get('ед'))
# выводим аналитику
for item in analytics:
    print(item, ':', list(analytics[item]))
