import time, random, requests
import logging
logging.basicConfig(filename="api-call-attempts.log",filemode='w',level=logging.INFO)
logger = logging.getLogger(__name__)

class RetryableError(Exception):
    '''
        Custom exception class for retry mechanism
    '''
    def __init__(self, *args):
        super().__init__(*args)
    
class FatalError(Exception):
    '''
        Custom exception class for retry mechanism
    '''
    def __init__(self, *args):
        super().__init__(*args)
    
def linear_delay(**kwargs):
    '''
        Handles the delay logic for linear backoff strategy
    '''
    time.sleep(1)

def exponential_delay(**kwargs):
    '''
        Handles the delay logic for exponential backoff strategy
    '''
    kwargs['prev_delay'][0] *= 2
    time.sleep(kwargs['prev_delay'][0])
    
def random_jitter_delay(**kwargs):
    '''
        Handles the delay logic for exponential random jitter backoff strategy
    '''
    kwargs['prev_delay'][0] *= 2
    time.sleep(kwargs['prev_delay'][0] + random.uniform(0,0.60))
    
backoff_handler = {
    'linear': linear_delay,
    'exponential': exponential_delay,
    'random jitter': random_jitter_delay
}

def retry_on_exception(max_attempts, backoff_strategy):
    '''
        Decorator function to emulate retry mechanism
        Takes in the max no of retry attempts and
        backoff strategy; valid ones are linear, exponential, random jitter
        Logs the attempts too
    '''
    def decorator(func):
        '''
        Second layer of nested decorator
        '''
        def wrapper(*args,**kwargs):
            '''                     
                Third layer of nested decorator and the actual wrapper func
            '''
            nonlocal max_attempts
            prev_delay = [0.5]
            for i in range(1,max_attempts+1):
                print(f"\nAttempt:{i}\n")
                try:
                    logger.info(f"Attempting function hit, Attempt no: {i}")
                    response = func(*args,**kwargs)
                except Exception as e:
                    logger.error(f"Ran into error: {e}")
                    if i == max_attempts:
                        raise
                    try:
                        backoff_handler[backoff_strategy.strip().lower()](prev_delay=prev_delay)
                    except KeyError:
                        raise FatalError('''
                        C'mon mate, provide a valid 
                        backoff strategy!
                                         ''')
                else:
                    return response.text
        
        return wrapper
    return decorator

@retry_on_exception(3,backoff_strategy='random jitter')
def api_call():
    '''
        Calls a GET api from jsonplaceholder website
        to get the post no 1
    '''
    result = requests.get('https://jsonplaceholder.typicode.com/po')
    result.raise_for_status() #404 errors are not raised by requests, so manually triggering them 
    return result

if __name__ == "__main__":
    print(api_call())