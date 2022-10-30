def get_count_char(str_):

    main_str_low = main_str.lower()
    main_list_low_alpha = []

    for i in main_str_low:
        if i.isalpha():
            main_list_low_alpha.append(i)

    dict_ = dict.fromkeys(main_list_low_alpha, 0)

    for i in main_list_low_alpha:
        for j in dict_:
            if j == i:
                dict_[j] += 1

    return dict_





main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""



print(get_count_char(main_str))


