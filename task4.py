'''
    Exercise 4: Function Argument Mastery
'''
import inspect

def merge_calls (*funcs, **defaults):
    '''
        A decorator to merge multiple func calls
        Funcs are executed in sequence and one func's output is passed as arg to another
    '''
    def wrapper(x,y):
        result = funcs[0](x,y)
        
        for i in range(1,len(funcs)):
            forward_kwargs = {}
            args_list = list(inspect.signature(funcs[i]).parameters.keys()) #returns the list of args for the given function
            
            for item in args_list:
                if item in defaults: 
                    forward_kwargs[item] = defaults[item] #if we have the keyword arg mentioned by func definition, we add it to forward kwargs
            
            if len(forward_kwargs) > 0:
                result = funcs[i](result, **forward_kwargs) #if we have the keyword arg, we pass it to function
            else:
                result = funcs[i](result)
        
        return result
    return wrapper

def add(x, y): return x + y

def multiply(x, factor=2): return x * factor

def exponent(x, exp=2): return x ** exp

if __name__ == "__main__":
    combined = merge_calls(add, multiply, exponent)
    result = combined(1, 2)
    
    print(result)