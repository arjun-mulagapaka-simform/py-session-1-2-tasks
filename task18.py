'''
    Task 18: Comparing performances of single-threaded,
    multi-threaded and multi-process approaches for
    CPU-bound task and I/O-bound task
'''
import time, math, concurrent.futures, requests, asyncio, aiohttp

loop = asyncio.get_event_loop()

def prime_number(n):
    '''
        Receives a number and returns True if prime
        otherwise False
    '''
    if n < 2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def get_image(size):
    '''
        Returns an image from the url
        `https://picsum.photos/{size}`\n
        400 is the base size and the
        passed arg is an offset
    '''
    response = requests.get(f'https://picsum.photos/{400+size}')
    return response.content

def get_tasks(session,sizes):
    tasks = []
    for size in sizes:
        tasks.append(
            loop.create_task(
                session.get(f'https://picsum.photos/{400+size}')
            )
        )
    return tasks

async def get_images():
    '''
        Async version for get_image func   
    '''
    images = []
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session,list(range(1,10)))
        responses = await asyncio.gather(*tasks)
        for response in responses:
            images.append(
                await response.read()
            )
    return images
        

if __name__ == "__main__":
    '''
        CPU-bound tasks
    '''
    # start_st = time.time()
    # primes_st = [n for n in range(1,1000001) if prime_number(n)]
    # print(f"--Prime numbers: Time taken in single thread = {time.time() - start_st}")
    
    # start_mt = time.time()
    # with concurrent.futures.ThreadPoolExecutor() as pool:
    #     results = list(pool.map(prime_number,range(1000001)))
    # primes_mt = [n for n,r in enumerate(results)
    #              if r]
    # print(f"--Prime numbers: Time taken in multithreading = {time.time() - start_mt}")
    
    '''without providing the chunksize arg to 
    processpoolexecutor.map, it takes insanse
    amount of time'''
    # start_mp = time.time()
    # with concurrent.futures.ProcessPoolExecutor() as pool:
    #     results_mp = list(pool.map(prime_number,range(1000001),chunksize=10000))
    # primes_mp = [n for n,r in enumerate(results_mp)
    #              if r]
    # print(f"--Prime numbers: Time taken in multiprocessing = {time.time() - start_mp}")
    
    '''
        I/O-bound tasks
    '''
    # start_st = time.time()
    # images_st = [get_image(i) for i in range(1,10)]
    # print(f"--Images download: Time taken in single thread = {time.time() - start_st}")
    
    # start_mt = time.time()
    # with concurrent.futures.ThreadPoolExecutor() as pool:
    #     images_mt = list(pool.map(get_image,range(1,10)))
    # print(f"--Images download: Time taken in multithreading = {time.time() - start_mt}")
    
    # start_async = time.time()
    # images_async = loop.run_until_complete(get_images())
    # print(f"--Images download: Time taken in asyncio = {time.time() - start_async}")
    
    loop.close()