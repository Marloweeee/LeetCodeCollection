# coding=utf-8
'''

模拟可知：灯泡状态的周期为6，且2和6、3和5受到相同的影响
也就是说，6个状态操作后其实只有4个状态
更进一步，当n>=3时，假设开关1、2、3、4分别操作了a、b、c、d次
灯泡1的状态=(1+a+c+d)%2；灯泡2的状态=(1+a+b)%2
灯泡3的状态=(1+a+c)%2；灯泡4的状态=(1+a+b+d)%2
当灯泡1==灯泡3时，d为偶数，则灯泡2和4的状态相同，反之则不同
那么，其实前3个灯泡状态就可以决定所有灯泡的状态


联想到线代中的线性相关，开关相当于向量运算，灯泡状态相当于向量运算后的结果
那么，4个开关操作所代表的向量可以用x1=[1,1,1,1];x2=[1,0,1,0];x3=[0,1,0,1];x4=[1,0,0,1]表示
那么灯泡状态可以用y=a1x1+a2x2+a3x3+a4x4来表示，a代表按键操作，只能为0或1
并且，当n>=3时，x1 x2 x4组成最大无关组
故解空间元素个数为2**3，最多有8种结果

'''


class Solution:
    def flipLights(self, n: int, presses: int) -> int:

        if presses==0:
            return 1
        if n==1:
            return 2
        if n==2:
            return 3 if presses==1 else 4
        return  8 if presses>2 else 4 if presses==1 else 7

if __name__ == '__main__':
    print(Solution().flipLights(3,4))