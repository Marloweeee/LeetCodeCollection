class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:

        base=minutesToTest//minutesToDie+1

        for i in range(buckets):
                if base**i>=buckets:
                    return i


if __name__ == '__main__':
    print(Solution().poorPigs(1,15,15))