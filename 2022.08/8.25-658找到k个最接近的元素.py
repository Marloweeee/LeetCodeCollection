from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        abs_dis=[abs(i-x) for i in arr]
        abs_dis,arr=zip(*sorted(zip(abs_dis,arr)))

        return sorted(arr[:k])



if __name__ == '__main__':
    print(Solution().findClosestElements([1,2,3,4,5],4,3))