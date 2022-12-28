per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму:'))
x = deposit_TKB = (money * 5.6 / 100)
y = deposit_SKB = (money * 5.9 / 100)
z = deposit_VTB = (money * 4.28 / 100)
e = deposit_SBER = (money * 4.0 / 100)
deposit_list = [x, y, z, e]
max_value = max(deposit_list)
print('Максимальная сумма которую вы сможете заработать', max_value)











