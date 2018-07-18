#!usr/bin/env python
# -*- coding: UTF-8 -*-

data_list = [2,3,4,5,1,2]

def find_duplication(data_list):  # O(nlogn) 不可改变输入数组 实现方法1
    if not data_list:
        return 'list is null'
    start = 1
    end = len(data_list)-1
    count = 0
    # 针对start-end的数据进行二分区间划分,并统计该区间内数字在集合中出现的次数
    while end >= start:
    	mid = (end-start)//2 +start
    	# (start,mid) (mid+1,end)
    	count = count_range(data_list, start, mid)
    	if end == start:
    		duplication = start if count>1 else -1
    		print('重复元素 %d' % duplication)
    		return 
    	if count > (mid-start+1):
    		# (start,mid)区间内有重复
    		end = mid
    	else:
    		start = mid +1

def count_range(data_list,start,end):
	count = 0
	for index in range(len(data_list)):
		# O(n)
		if start<=data_list[index]<=end:
			count+=1
	return count

def find_duplication_more_time(data_list):  # O(n^2) 实现方法2
    for index in range(len(data_list)):
        if data_list.count(data_list[index])>1:
            print('重复元素 %d 重复次数 %d' % (data_list[index], data_list.count(data_list[index])))

def find_duplication_change(data_list):  # 实现方法3,前提是如果可以改变输入数组 O(n) 让i位置存储value=i的元素
    for i in range(len(data_list)):
        while data_list[i] != i:
            if data_list[i] == data_list[data_list[i]]:
            	print('重复元素 %d' % data_list[i])
            	break
            temp = data_list[i]
            data_list[i] = data_list[temp]
            data_list[temp] = temp


find_duplication(data_list)
find_duplication_more_time(data_list)
find_duplication_change(data_list)