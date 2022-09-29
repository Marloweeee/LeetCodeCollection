from typing import List
class Solution:
    def Partition(self,arr:List[int],low:int,high:int) -> int:
        arr[0]=arr[low]
        while(low<high):
            while(low<high and arr[0]<=arr[high]):high-=1
            arr[low]=arr[high]
            while(low<high and arr[0]>=arr[low]):low+=1
            arr[high]=arr[low]
        arr[low]=arr[0]
        return low
    def QuickSort(self,arr:List[int],low:int,high:int):
        if(low<high):
            position=Solution().Partition(arr,low,high)
            Solution().QuickSort(arr,low,position-1)
            Solution().QuickSort(arr,position+1,high)

    def smallestK(self, arr: List[int], k: int) -> List[int]:
        low,high=1,len(arr)
        num=[0]
        for i in arr:
            num.append(i)
        Solution().QuickSort(num,low,high)
        return num[1:k+1]
if __name__ == '__main__':
    arr ,k= [1, 3, 5, 7, 2, 4, 6, 8] , 6
    s=Solution()
    print(s.smallestK(arr,k))
