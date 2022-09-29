# -*- coding: utf-8 -*-
from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        idx,sentence,length=0,[],len(words)
        while idx<length:
            temp,temp_len=[],0
            while idx<length and temp_len+len(words[idx])<=maxWidth:
                temp.append(words[idx])
                temp_len+=len(words[idx])+1
                idx+=1
            sentence.append(temp)
        # return sentence
        res=[]
        for i in range(len(sentence)-1):
            # 处理只有一个单词的句子
            if len(sentence[i])==1:
                res.append(sentence[i][0]+" "*(maxWidth-len(sentence[i][0])))
                continue

            # 处理包含多个单词的句子
            totle_len,num=0,0
            for j in range(len(sentence[i])):
                totle_len+=len(sentence[i][j])
                num+=1
            base=(maxWidth-totle_len)//(num-1)# 基准空格
            one_more=(maxWidth-totle_len)%(num-1)# 多余空格
            word=''
            for j in range(one_more):
                word+=sentence[i][j]+" "*(base+1)
            for j in range(one_more,len(sentence[i])-1):
                word+=sentence[i][j]+" "*base
            word+=sentence[i][-1]
            res.append(word)

        #处理最后一个句子
        temp=sentence[-1][0]
        temp_len=len(temp)
        for i in range(1,len(sentence[-1])):
            temp+=" "+sentence[-1][i]
            temp_len+=len(sentence[-1][i])+1
        temp+=" "*(maxWidth-temp_len)
        res.append(temp)
        return res


if __name__ == '__main__':
    words,maxWidth=["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],20
    print(Solution().fullJustify(words,maxWidth))
