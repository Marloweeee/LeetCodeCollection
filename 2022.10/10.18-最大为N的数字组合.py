from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # 数位DP（记忆化搜索模板）

        s = str(n)  # 将整数n转为字符型

        def f(i: int, is_limit: bool, is_number: bool) -> int:

            if i == len(s):
                return int(is_number)
            res = 0
            if not is_number:  # 选择跳过，不填数字
                res = f(i + 1, False, False)

            up = int(s[i]) if is_limit else '9'
            for d in digits:
                if d>up:break
                res += f(i + 1,is_limit and d == up, True)
            return res

        return f(0, True, False)