class FibonacciIterator:
    def __init__(self, count):
        self.count = count
        self.index = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < self.count:
            result = self.b
            self.a, self.b = self.b, self.a + self.b
            self.index += 1
            return result
        else:
            raise StopIteration

class Solution:
    def fib(self, n: int) -> int:
        fib_iter = FibonacciIterator(n)
        for num in fib_iter:
            if fib_iter.index == n:
                return num
        return 0