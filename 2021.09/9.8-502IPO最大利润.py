import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w>max(capital):
            return sum(heapq.nlargest(k,profits))
        n=len(profits)
        curr=0
        arr=[(capital[i],profits[i]) for i in range(n)]
        arr.sort(key=lambda x:x[0])

        pq=[]
        for _ in range(k):
            while curr<n and arr[curr][0]<=w:
                heapq.heappush(pq,-arr[curr][1])
                curr+=1
            if pq:
                w-=heapq.heappop(pq)
            else:break
        return w

if __name__ == '__main__':
    k,w,profits,capital=2,0,[1,2,3],[0,1,1]
    print(Solution().findMaximizedCapital(k,w,profits,capital))