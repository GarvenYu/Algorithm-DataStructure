#! usr/bin/env python
# -*-coding:utf-8-*-

def FibonacciRecursion(n):
	"""斐波那契数列递归解法,复杂度O(n^n)"""
	if n==0:
		return n
	elif n==1:
		return n
	else:
		return FibonacciRecursion(n-1)+FibonacciRecursion(n-2)


def FibonacciNotRecursion(n):
    """
	斐波那契数列非递归解法
    自下而上计算,保存计算结果,复杂度O(n)   
    """
    f = [0, 1]
    if n <=1:
        return f[n]
    else:
        a = f[0]
        b = f[1]
        i = 1
        while i < n:
            result = b + a
            a = b
            b = result
            i+=1
        return result


if __name__ == '__main__':
    print(FibonacciRecursion(6))
    print(FibonacciNotRecursion(6))
