class Solution(object):
    def arrayRankTransform(self, arr):
        n = len(arr)
        list1 = []
        arr1 = sorted(set(arr))

        rank = {}
        for j in range(len(arr1)):
            rank[arr1[j]] = j + 1

        for i in range(n):
            list1.append(rank[arr[i]])

        return list1
