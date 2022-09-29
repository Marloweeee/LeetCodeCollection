from typing import List

class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:

        sum_num=sum([i for i in nums])
        two_num=(len(nums)+2)*(len(nums)+3)/2-sum_num


        limits,tmp_sum=int(two_num/2),0
        for i in nums:
            if i<=limits:
                tmp_sum+=i
        one_num=int(limits*(limits+1)/2-tmp_sum)
        another_num=int(two_num-one_num)

        return [one_num,another_num]



if __name__ == '__main__':
    print(Solution().missingTwo([1]))