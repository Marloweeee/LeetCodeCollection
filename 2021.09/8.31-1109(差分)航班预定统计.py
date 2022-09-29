from typing import List
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res=[0 for i in range(n)]
        for left,right,seats in bookings:
            res[left-1]+=seats
            if right<n:
                res[right]-=seats


        for i in range(1,len(res)):
            res[i]+=res[i-1]
        return res
if __name__ == '__main__':
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    s=Solution()
    print(s.corpFlightBookings(bookings,n))

