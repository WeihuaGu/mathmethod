# coding=utf-8
def left_list(value, raw):
    return [item for item in raw if item!= value]
def print_byline(list):
    for item in list:
        print(item)

#递归实现的全排列
def full_permutation(current_list):
    listlen = len(current_list)
    if listlen > 1:
        current_result_list=[]
        for element in current_list:
            next_sub_list = left_list(element, current_list)
            for one_permutate in full_permutation(next_sub_list):
                one_permutate.insert(0,element)
                current_result_list.append(one_permutate)
        return current_result_list


    else:
        return [ current_list ]

my_list = ['甲','乙','丙','丁']
result_permutation=full_permutation(my_list)
print_byline(result_permutation)


