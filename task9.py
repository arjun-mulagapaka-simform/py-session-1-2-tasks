'''
    Exercise 9: Custom Decorators Chain
    
    Nested decorators function execution sequence:
    timer -> retry -> cache -> validate types -> actual function -> 
    return result to validate types -> return result to cache ->
    return result to retry -> return result to timer ->
    return result to main
'''

from functools import wraps
import time

memo = {} #cache store

def timer(func):
    '''
        A decorator function to measure the time taken in execution by the passed function
    '''
    @wraps(func) #this ensures that the function passed to wrapper for execution is the actual func and not the previous level's wrapped func
    def wrapper(*args,**kwargs):
        '''
            timer decorator's wrapper
        '''
        print("---Inside timer---")
        t1 = time.time()
        try:
            result = func(*args,**kwargs) #get result from function call, btw this calls retry deco, meaning we are going down the levels
        except Exception:
            raise
        finally:
            print(f"execution_time = {time.time() - t1}")
        return result #return result to main, this gets result from retry deco, meaning we are returning result upwards through the levels
    return wrapper

def retry(attempts=3,delay=1):
    '''
        A decorator function to retry the execution of passed func specified no of times
    '''
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            '''
                retry decorator's wrapper
            '''
            print("---Inside retry---")
            nonlocal attempts
            while attempts > 0:
                try:
                    return func(*args,**kwargs) #return result to timer deco, this gets result from cache deco, meaning we are returning result upwards through the levels
                except Exception:
                    time.sleep(delay)
                    attempts -= 1 #everytime the function call fails, deduct an attempt
                    if attempts == 0:
                        raise
        return wrapper
    return decorator

def cache(func):
    '''
        A decorator function to store the func results in a cache kind of system
    '''
    @wraps(func)
    def wrapper(*args,**kwargs):
        '''
            cache decorator's wrapper
        '''
        print("---Inside cache---")
        if 'Result' in memo.keys():
            return memo['Result']
        else:
            try:
                result = func(*args,**kwargs) #get result from function call, btw this calls validate types deco, meaning we are going down the levels
            except Exception:
                raise
            else:
                memo['Result'] = result
            return result #return result to retry deco, this gets result from validate types deco, meaning we are returning result upwards through the levels
    return wrapper

def validate_types(**type_hints):
    '''
        A decorator function to validate the arg types passed to the function
    '''
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            '''
                validate_types decorator's wrapper
                takes in kwargs which specify the required types of the args to be passed
            '''
            print("---Inside validate types---")
            for key in kwargs.keys():
                if not type(kwargs[key]) == type_hints[key]:
                    raise TypeError(f"{key} expected value of type {type_hints[key]}")
              
            try:
                result = func(*args,**kwargs) #get result from function call, btw this calls validate types deco, meaning we are going down the levels
            except Exception:
                raise
            return result #return result to retry deco, this gets result from validate types deco, meaning we are returning result upwards through the levels
        return wrapper
    return decorator

# Simulating a slow API call with sleep
@timer
@retry(attempts=3, delay=1)
@cache
@validate_types(data_type=str)
def fetch_data_from_api(data_type):
    print(f"Fetching data of type: {data_type}")
    time.sleep(2)  # Simulate slow API response
    raise PermissionError("***You cannot execute this function***")
    #return f"Fetched data of type {data_type}"

def main():
    try:
        # Call the fetch_data_from_api function
        result = fetch_data_from_api("json")
        print(f"Result: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()