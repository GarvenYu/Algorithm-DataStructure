def last_sort(str1, str2):
    if len(str2) <= 1:
        return str2
    else:
        return last_sort(str1[1:str2.index(str1[0])+1], str2[:str2.index(str1[0])]) \
            + last_sort(str1[str2.index(str1[0])+1:],
                        str2[str2.index(str1[0])+1:]) + str1[0:1]


str1 = ['A', 'B', 'D', 'C', 'E', 'F']  # 前序遍历
str2 = ['D', 'B', 'A', 'E', 'C', 'F']  # 中序遍历
print(last_sort(str1, str2))
