"""
制作一个新的列表
从第二项开始遍历l
  拿到第二个元素e
  开始遍历之前的元素
    比较e和之前的元素
    如果小于
      放在前面
    如果不小于
      继续比较
    如果都不小于
      放在最后面
"""
import copy


def InsertSort(nums: list) -> list:
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            print(nums[i])
            for j in range(i):
                if nums[i] < nums[j]:
                    nums.insert(j, nums[i])
                    nums.pop(i+1)

    return nums


l = [34, 85, 9, 346, 111, 1, 94]
nums = InsertSort(l)
print(nums)