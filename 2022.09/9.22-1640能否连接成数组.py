from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:

        arr_left=0
        index = {p[0]: i for i, p in enumerate(pieces)}

        while arr_left<len(arr):
            if arr[arr_left] not in index:
                return False
            else:
                item=pieces[index[arr[arr_left]]]
                if arr[arr_left:arr_left+len(item)]!=item:
                    return False
                arr_left+=len(item)
        return True


if __name__ == '__main__':
    arr = [15, 88,99]
    pieces = [[99,88], [15]]
    print(Solution().canFormArray(arr,pieces))