from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length=len(arr)
        sum=0
        epochs=(length+1)/2
        for epoch in range(epochs):
            for step in range(1,length+1,2):
                print(1)

arr=[1,4,2,5,3]
s=Solution()
s.sumOddLengthSubarrays(arr=arr)