"""
做一个和l一摸一样的矩阵M
然后每个点位都要保留所有可能路径的路程信息
开始遍历M
  每一个点来源于之前的路径

"""
import copy


def InsertSort(nums: list) -> list:
    M = copy.copy(nums)
    M[0][0] = [[0]]

    for i, line in enumerate(M):
        for j, one in enumerate(line):
            print(nums[i][j])
            if i == 0 and j != 0:
                M[i][j] = M[i][j-1] + [nums[i][j]]
                print(M)
            if j == 0 and i != 0:
                M[i][j] = M[i-1][j] + [nums[i][j]]
                print(M)
            M[i][j] = []
            M[i][j].append(M[i][j-1] + [nums[i][j]])
            M[i][j].append(M[i-1][j] + [nums[i][j]])


    return 0


l = [[0, 6, 2],
     [3, 4, 10],
     [22, 78, 1]]

nums = InsertSort(l)
print(nums)