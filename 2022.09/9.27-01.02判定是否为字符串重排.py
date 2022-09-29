class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:

        len1,len2=len(s1),len(s2)
        if len1!=len2:
            return False

        s1_dic={}# 为s1建立存储字符与出现次数的字典
        for item in s1:
            if item in s1_dic:
                s1_dic[item]+=1
            else:
                s1_dic[item]=1

        for item in s2:
            if item not in s1_dic:
                return False
            s1_dic[item]-=1

        min_num,max_num=min(s1_dic.values()),max(s1_dic.values())
        if min_num!=max_num:
            return False
        return True

if __name__ == '__main__':
    s1='aabbjklkjh'
    s2='jklkjhaabb'
    print(Solution().CheckPermutation(s1,s2))
