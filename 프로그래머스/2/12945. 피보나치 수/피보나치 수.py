class FibonacciIterator:
    def __init__(self,count):
        self.count=count
        self.index=0
        self.a,self.b=0,1

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
            
def solution(n):
    for i in FibonacciIterator(n):
        answer=i
    return answer%1234567