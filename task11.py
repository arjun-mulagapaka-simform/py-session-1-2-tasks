'''
    Exercise 11: Custom Iterator - Fibonacci
'''
import sys

class Fibonacci:
    '''
        An iterator class for generating fibonacci numbers
    '''
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        return self
    
    def __next__(self):
        x = self.n1
        self.n1, self.n2 = self.n2, self.n1+self.n2
        return x
    
def fibonacci_gen(limit):
    '''
        A generator function for fibonacci sequence
    '''
    x,y = 0,1
    for _ in range(0,limit):
        yield x
        x,y = y,x+y
    
if __name__ == "__main__":
    fib = Fibonacci()
    it = iter(fib)
    print("Through iterator class")
    for i in range(1,1000):
        print(next(it))
    
    print("\nThrough generator function")
    for i in fibonacci_gen(1000):
        print(i)
    