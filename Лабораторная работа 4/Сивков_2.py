def get_count_char(str_):
    str_ = str_.lower()
    glossar = {}
    DEF_ = 0
    for letter in str_:
        if letter.isalpha():
            glossar[letter] = glossar.get(letter, DEF_) + 1
    return glossar

def new_glossar(glossar):
    total_count = sum(glossar.values())
    for count in glossar:
        glossar[count] = round(glossar.get(count) / total_count * 100, 2)
    return glossar

# TODO посчитать количество каждой буквы в строке в аргументе str_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
result_1 = get_count_char(main_str)
print(get_count_char(main_str))
print(new_glossar(result_1))
