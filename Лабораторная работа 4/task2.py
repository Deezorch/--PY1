def get_count_char(str_):

    main_str_low = str_.lower()
    dict_ = {}
    def_count = 0

    for i in main_str_low:
        if i.isalpha():
           dict_[i] = dict_.get(i, def_count) + 1

    return dict_

def get_count_char_interest(str_):

    main_str_low = str_.lower()
    dict_ = {}
    def_count = 0

    for i in main_str_low:
        if i.isalpha():
           dict_[i] = dict_.get(i, def_count) + 1

    for i in dict_:
        dict_[i] = round(dict_[i] / sum(dict_.values()) * 100, 2)

    return dict_



main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""



print(get_count_char(main_str))


