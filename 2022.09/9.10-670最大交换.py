# coding=utf-8

# 从数字的个位开始，依次往后寻找大于当前数字的最大值，并且当出现重复值时选择重复值的最后一位

class Solution:
    def maximumSwap(self, num: int) -> int:
        num=str(num)
        length=len(num)

        for idx in range(length):
            max_num,change_idx,max_idx=num[idx],idx+1,0
            while change_idx<length:
                if num[change_idx]>max_num:
                    max_num=num[change_idx]
                    max_idx=change_idx
                    change_idx+=1
                else:
                    change_idx+=1

            if max_num>num[idx]:
                tmp_idx=max_idx+1
                while tmp_idx<length :
                    if num[max_idx]==num[tmp_idx]:
                        max_idx=tmp_idx
                        tmp_idx+=1
                    else:
                        tmp_idx+=1

                num=list(num)
                num[max_idx],num[idx]=num[idx],max_num
                break
        return int(''.join(num))




if __name__ == '__main__':
    print(Solution().maximumSwap(10909091))
