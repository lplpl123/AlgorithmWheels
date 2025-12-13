"""
做一个和l一摸一样的矩阵M
然后每个点位都要保留所有可能路径的路程信息
开始遍历M
  每一个点来源于之前的路径

"""
import copy


def InsertSort(nums: list) -> list:
    M = copy.deepcopy(nums)
    M[0][0] = [[0]]

    for i, line in enumerate(M):
        for j, one in enumerate(line):
            print(nums[i][j])
            if i == 0 and j != 0:
                M[i][j] = copy.deepcopy(M[i][j-1])
                for lastData in M[i][j]:
                    lastData.append(nums[i][j])
            if j == 0 and i != 0:
                M[i][j] = copy.deepcopy(M[i-1][j])
                for lastData in M[i][j]:
                    lastData.append(nums[i][j])

            if i != 0 and j != 0:
                pathOne = copy.deepcopy(M[i][j-1])
                print(pathOne)
                pathTwo = copy.deepcopy(M[i-1][j])
                print(pathTwo)
                M[i][j] = []
                for data in pathOne:
                    data.append(nums[i][j])
                    M[i][j].append(data)
                for data in pathTwo:
                    data.append(nums[i][j])
                    M[i][j].append(data)
            print(M)
            print("------over------")


    return 0


l = [[0, 6, 2],
     [3, 4, 10],
     [22, 78, 1]]

nums = InsertSort(l)
print(nums)