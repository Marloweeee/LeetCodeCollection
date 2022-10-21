class StockSpanner:

    def __init__(self):
        self.stack=[]


    def next(self, price: int) -> int:

        # 使用单调栈进行解答
        sum_span=1

        while self.stack and self.stack[-1][0]<=price:
            sum_span+=self.stack.pop()[1]

        self.stack.append((price,sum_span))
        return sum_span

if __name__ == '__main__':
    pass




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)