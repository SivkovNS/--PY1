def delete(list_, index=None):
    len_ = len(list_)
    if index == None:
        b = len_-1
        result_ = list_[:b]
    else:
        a = index + 1
        p_1 = list_[:index]
        p_2 = list_[a:]
        result_ = p_1 + p_2
    return result_
    # TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
