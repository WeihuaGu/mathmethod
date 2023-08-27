# coding=utf-8
import math
def generate_permutations(colors, num_positions):
    if num_positions == 0:
        return [[]]  # 返回一个空列表，表示没有位置的情况

    if num_positions == 1:
        return [[color] for color in colors]  # 返回单个位置的颜色排列

    permutations = []
    smaller_permutations = generate_permutations(colors, num_positions - 1)
    for color in colors:
        for smaller_permutation in smaller_permutations:
            permutations.append([color] + smaller_permutation)

    return permutations

def find_index(lst, value):
    try:
        index = lst.index(value)
        return index+1;
    except ValueError:
        return -1  # 如果值不在列表中，则返回 -1


def apply_permutation(chars, permutation):
    p_chars = list(chars)
    
    # 分割不同的括号组
    parentheses_groups = []
    current_group = ""
    open_parentheses = 0
    for char in permutation:
        if char == '(':
            open_parentheses += 1
        elif char == ')':
            open_parentheses -= 1

        current_group += char

        if open_parentheses == 0:
            if current_group != ",":
                parentheses_groups.append(current_group)
            current_group = ""

    # 将每个括号组中的元素入队列
    queues = []
    for group in parentheses_groups:
        group_chars = list(group.strip('()'))
        if ',' in group_chars:
            group_chars.remove(',')
        if ' ' in group_chars:
            group_chars.remove(' ')
        queue = [int(x) - 1 for x in group_chars if x is not None and x.strip() != '' and x != ',']
        if len(queue)>0:
            queues.append(queue)

    # 从队列中依次取出元素进行变换
    for queue in queues:
      if len(queue)>1:
          isone = False;
      else:
          isone = True;
      first_index = queue[0]
      while True:
        from_index = queue.pop(0)
        if len(queue) == 0:
            if isone:
                p_chars[from_index] = chars[from_index]
            else:
                p_chars[first_index] = chars[from_index]
        else:
            p_chars[queue[0]]=chars[from_index]
        if not queue:
            break

    return p_chars

def generate_An(n):
    def backtrack(nums, start):
        if start == len(nums):
            permutations.append(nums[:])
        else:
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(nums, start + 1)
                nums[start], nums[i] = nums[i], nums[start]

    permutations = []
    nums = list(range(1, n + 1))
    backtrack(nums, 0)

    def format_permutation(permutation):
        cycles = []
        visited = [False] * len(permutation)

        for i in range(len(permutation)):
            if not visited[i]:
                cycle = [i + 1]
                visited[i] = True
                j = permutation[i] - 1

                while j != i:
                    cycle.append(j + 1)
                    visited[j] = True
                    j = permutation[j] - 1

                cycles.append(cycle)

        formatted = ', '.join(['(' + ', '.join(map(str, cycle)) + ')' for cycle in cycles])
        return formatted

    formatted_permutations = [format_permutation(perm) for perm in permutations]
    return formatted_permutations

def find_factorial_number(M):
    n = 0  # 初始化数字 n

    while True:
        n += 1
        factorial = math.factorial(n)

        if factorial == M:
            return n
def fix(g,listset):
    num = 0;
    K_result = [];
    print('对g=%s的所有置换不变的Klist:' % (g));
    for one_k in listset:
        output_string = apply_permutation(one_k, g)
        if one_k == output_string :
            num = num+1;
            K_result.append(one_k)
    return K_result


def Zk(k,G):
    num = 0;
    Z_result = [];
    Klist = list(k);
    print('对k=%s的所有A%d不变置换Zk:' % (k,find_factorial_number(len(G))));
    for one_g in G:
        #print(one)
        output_string = apply_permutation(k, one_g)
        #print(output_string)
        if Klist == output_string:
            num = num+1;
            #print(one+'是'+K+'的不动点置换')
            Z_result.append(one_g);
    return Z_result;
def Ek(k,G):
    num = 0;
    Z_result = [];
    Klist = list(k);
    print('对k=%s的所有A%d置换的Klist:' % (k,find_factorial_number(len(G))));
    for one_g in G:
        output_string = apply_permutation(k, one_g)
        Z_result.append(output_string);
    return set(map(tuple, Z_result))

def merge_sets(my_list):
    merged_list = []

    for s in my_list:
        is_merged = False
        for m in merged_list:
            if s == m:
                is_merged = True
                break
        if not is_merged:
            merged_list.append(s)

    return merged_list

# 示例用法
n = 3
A3 = generate_An(n)
Klist = generate_permutations(['R','B'],3)
Ex = []
for one_k in Klist:
    r_Ek=Ek(one_k,A3);
    Ex.append(r_Ek);
    r_Zk=Zk(one_k,A3);
    print(r_Ek)
    print(r_Zk)
    print('Ek数量%d * Zk数量%d = %d ' %(len(r_Ek),len(r_Zk),len(r_Ek)*len(r_Zk)))
    print('\n');
Exset = merge_sets(Ex)
print('等价类个数为%d' %(len(Exset)))
for oneset in Exset:
    print(oneset)

print('\n');


for one_g in A3:
    print(fix(one_g,Klist))
    print('\n');
