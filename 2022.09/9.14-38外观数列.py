class Solution:
    def countAndSay(self, n: int) -> str:

        if n==1:
            return "1"

        def get_next_num(num):
            left, length ,res= 0, len(num),""

            while left < length:
                right = left + 1
                while right < length and num[right] == num[left]:
                    right += 1
                res = res + str(right - left) + num[left]
                left = right
            return res

        ans=[0 for i in range(n+1)]
        ans[0]=get_next_num("1")

        for idx in range(1,n):
            ans[idx]=get_next_num(ans[idx-1])

        return ans[n-2]




if __name__ == '__main__':
    print(Solution().countAndSay(5))