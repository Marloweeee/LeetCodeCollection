# coding=utf-8

class Solution:
    def reorderSpaces(self, text: str) -> str:

        '''
        :param text: 包含多个空格的字符串
        :return: 空格平均分布后的字符串
        '''

        length=len(text)
        words,spaces=0,0
        for pre in range(length-1):
            if text[pre]!=' ' and text[pre+1]==' ':
                words+=1
            if text[pre]==' ':
                spaces+=1
        if text[-1]==' ':
            spaces+=1
        print(words,spaces)
        # if words==1:
        #     return

        each_space=spaces//(words-1)
        end_space=spaces-each_space*(words-1)
        print(each_space,end_space)

        res=''
        for pre in range(length-1):

            if text[pre]!=' ':
                res+=text[pre]
                print("字母：{}".format(res))
            if text[pre]!=' ' and text[pre+1]==' ':
                res.append(' '*end_space)
                print("空格：{}".format(res))

        if text[-1]!=' ':
            res+=text[-1]

        res+=' '*end_space

        return res
if __name__ == '__main__':

    print(Solution().reorderSpaces("  this   is  a sentence "))

