from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res=1
        for item in nums:
            res*=1 if item>0 else -1 if item<0 else 0
        return res


'''java

class Solution {
    public int arraySign(int[] nums) {

        int res=1;
        for(int i=0;i<nums.length;i++)
            res*=nums[i]>0?1:nums[i]<0?-1:0;
        return res;
    }
}

'''

'''cpp

class Solution {
public:
    int arraySign(vector<int>& nums) {
        int length=nums.size();
        int sum=1;
        for (int i=0;i<length;i++){
            if (nums[i]>0)
                sum*=1;
            else if (nums[i]<0)
                sum*=-1;
            else
                sum*=0;
        }

        return sum;

    }
};

'''