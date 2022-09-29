from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()

        start_idx,end_idx,sum_arr=len(arr)//20,len(arr)-len(arr)//20,0
        for idx in range(start_idx,end_idx):
            sum_arr+=arr[idx]

        return sum_arr/(end_idx-start_idx)

if __name__ == '__main__':
    arr = [9, 7, 8, 7, 7, 8, 4, 4, 6, 8, 8, 7, 6, 8, 8, 9, 2, 6, 0, 0, 1, 10, 8, 6, 3, 3, 5, 1, 10, 9, 0, 7, 10, 0, 10,
           4, 1, 10, 6, 9, 3, 6, 0, 0, 2, 7, 0, 6, 7, 2, 9, 7, 7, 3, 0, 1, 6, 1, 10, 3]

    print(Solution().trimMean(arr))