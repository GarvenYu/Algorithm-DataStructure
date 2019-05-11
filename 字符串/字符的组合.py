def combine(param):
    """

    :param param: [str]
    """
    if not param:
        return param
    length = len(param)
    ans = []
    for i in range(1, length + 1):
        ans += combine_core(param, i)
    print(ans)


def combine_core(param, out_length):
    if out_length == 0:
        return []
    if len(param) == out_length:
        return [''.join(param)]
    if len(param) > out_length:
        a = [param[0]] + combine_core(param[1:], out_length - 1)
        for i in range(1, len(a)):
            # 例如寻找长度为2的子组合时,a=['a', 'b', 'c'],实际需要的是['ab','ac']
            a[i] = a[0] + a[i]  # ['a', 'ab', 'ac']
        if len(a) > 1:
            a.pop(0)
        b = combine_core(param[1:], out_length)
        return a + b


p = ['a', 'b', 'c', 'd']
combine(p)  # output ['a', 'b', 'c', 'd', 'ab', 'ac', 'ad', 'bc', 'bd', 'cd', 'abc', 'abd', 'acd', 'bcd', 'abcd']
