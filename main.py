print('module_1_5.py')
immutable_var_tuple = 1, 2, 'a', type
print("immutable_var tuple: ", immutable_var_tuple)
# Изменить элемент кортежа нельзя, т.к. кортеж не поддерживает обращение по элементам.
mutable_list = [0, [1, 2], 'a', True]
print('mutable_list:', mutable_list)
# Иэменения элементов списка
mutable_list [1][0] = 3
mutable_list [2] = 'b'
print(mutable_list)
mutable_list = [0, [1, 2], 'a', True] + [False]
print('Конкатенация: ', mutable_list)
