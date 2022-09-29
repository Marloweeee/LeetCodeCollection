# 1 (rand_X() - 1) × Y + rand_Y() ==> 可以等概率的生成[1, X * Y]范围的随机数，即rand_XY()
# 2 若M是N的倍数，则rand_M()%N+1可以产生[1,N]范围的随机数
# 3 当M不是N的倍数时，采用拒绝采样方法，即判断M=(rand_N()-1)*N+rand_N()是否在N的倍数范围内，是则返回M%N+1


# The rand7() API is already defined for you.
def rand7():
    pass
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            num=(rand7()-1)*7+rand7()# [1,49]
            if num<=40:
                return num%10+1
        