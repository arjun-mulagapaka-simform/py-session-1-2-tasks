'''
    Exercise 3: Advanced List Comprehension with Filters
'''
import sys

if __name__ == "__main__":
    lst = [x**2 for x in list(filter(lambda i: (i%3 == 0 or i%5 == 0) and i%15 != 0, [list(range(1,101))] )) if x**2 < 1000] #list comprehension
    
    print(*lst)
    print("Size from list comprehension is:",sys.getsizeof(lst), "bytes")
    
    #generator expr, notice the round brackets around ranges
    generator_lst = (x**2 for x in list(filter(lambda i: (i%3 == 0 or i%5 == 0) and i%15 != 0, (x for x in range(1,101)) )) if x**2 < 1000)
    
    print("\n",*generator_lst)
    print("Size from generator expression is:",sys.getsizeof(generator_lst), "bytes")