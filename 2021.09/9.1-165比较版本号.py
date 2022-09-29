class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1,version2=list(map(int,version1.split('.'))),list(map(int,version2.split('.')))
        length=min(len(version1),len(version2))

        for idx in range(length):
            if version1[idx]>version2[idx]:
                return 1
            elif version1[idx]<version2[idx]:
                return -1
        if len(version1)>length:
            sum_num=sum(version1[length:])
            if sum_num>0:
                return 1
        if len(version2)>length:
            sum_num=sum(version2[length:])
            if sum_num>0:
                return -1
        return 0
if __name__ == '__main__':
    version1 = "1.1.0"
    version2 = "1.001.00.1"
    s=Solution()
    print(s.compareVersion(version1,version2))
