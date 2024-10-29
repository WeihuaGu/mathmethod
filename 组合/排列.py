# coding=utf-8
def last_list(value, raw):
    return [item for item in raw if item!= value]

def full_permutation(current_list,n):
    listlen = len(current_list)
    if listlen > 1:
        result_list=[]
        for element in current_list:
            next_list = last_list(element, current_list)
            for one_permutate in full_permutation(next_list,listlen-1):
                one_permutate.insert(0,element)
                result_list.append(one_permutate)
        return result_list


    else:
        return [ current_list ]

my_list = [1, 2, 3, 5, 4]
result=full_permutation(my_list,len(my_list))
print(len(result))
print(result)


