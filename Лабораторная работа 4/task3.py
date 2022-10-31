def delete(list_, index=-1):
    if index >= 0:
        list_1 = list_[:index]
        list_2 = list_[index + 1:]
        return list_1 + list_2

    else:
        list_1 = list_[:index + len(list_)]
        list_2 = list_[index + 1 + len(list_):]
        return list_1 + list_2




print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]

# for i in range(-len(list_), len(list_), 1):
#    print(delete(list_, i))
# Предлагаю изменить вашу проверку на эту, тк она учитывает все частные случаи. Например index = -1
