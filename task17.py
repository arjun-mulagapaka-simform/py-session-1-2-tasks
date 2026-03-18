import asyncio, aiohttp, csv
from bs4 import BeautifulSoup

urls = [
    'https://www.msn.com/en-us/sports/soccer/man-city-knocked-out-of-champions-league-by-real-madrid-again/ar-AA1YQpLZ?ocid=BingNewsVerp',
    'https://www.moneycontrol.com/sports/champions-league-real-madrid-psg-advance-to-quarterfinals-manchester-city-chelsea-out-article-13863696.html',
    'https://www.nytimes.com/athletic/live-blogs/manchester-city-vs-real-madrid-live-updates-champions-league-score-result/AuGiBEjND0ZB/',
    'https://www.outlookindia.com/sports/football/manchester-city-vs-real-madrid-live-score-uefa-champions-league-2025-26-round-of-16-second-leg-updates-highlights-etihad-stadium',
    'https://www.msn.com/en-us/sports/soccer/man-city-knocked-out-of-champions-league-by-real-madrid-again/ar-AA1YQpLZ?ocid=BingNewsVerp',
    'https://www.msn.com/en-us/sports/soccer/man-city-vs-real-madrid-live-latest-updates-from-champions-league-ro16-second-leg/ar-AA1YQgiK?ocid=BingNewsVerp',
    'https://www.channelstv.com/2026/03/17/real-madrid-dump-man-city-out-of-champions-league/',
    'https://www.hindustantimes.com/sports/football/real-madrid-batter-manchester-city-as-psg-sink-chelsea-in-champions-league-101773281508276.html',
    'https://www.msn.com/en-us/sports/soccer/vinicius-junior-s-brace-sends-real-madrid-into-champions-league-quarterfinals-with-2-1-win-over-manchester-city/ar-AA1YQ8r3?ocid=BingNewsVerp',
    'https://www.msn.com/en-in/news/world/real-madrid-run-riot-as-valverde-treble-stuns-man-city/ar-AA1Yqc2C?ocid=BingNewsVerp',
    'https://www.bing.com/aclk?ld=e87uCUMBOMLIsfWs6wX-19qjVUCUzGGuZmu1JbiitfbQhqvmmx20DVU29vxVb5DSug5xux25UB2c6U3opjDytHSRut-JOuOYc3AMspLo88VSSfA5W4TPK0jlSDbn3e4XdLsbrDTY5vKwEbnhYtQgnkvdMcorbhCk4Jv_7dMpLwY14TNYPzuZzYu0qEqkJBY_dcofY_OogvhbBjRqp-Yra27bLShK0&u=aHR0cHMlM2ElMmYlMmZ3d3cuZ2V0eW91cmd1aWRlLmNvbSUyZi1sNDYlMmYlM2ZjbXAlM2RiaW5nJTI2Y21wJTNkYmluZyUyNmFkX2lkJTNkNzgzNDA0MjI4NTQ2NjUlMjZhZGdyb3VwX2lkJTNkMTI1MzQ0NDYxMzg2MTI0MiUyNmJpZF9tYXRjaF90eXBlJTNkYmUlMjZjYW1wYWlnbl9pZCUzZDcxMDgxODM5NiUyNmRldmljZSUzZGMlMjZmZWVkX2l0ZW1faWQlM2QlMjZrZXl3b3JkJTNkbWFkcmlkJTI1MjBlcyUyNmxvY19pbnRlcmVzdF9tcyUzZDE2NDM2MyUyNmxvY19waHlzaWNhbF9tcyUzZDE1ODM3MSUyNm1hdGNoX3R5cGUlM2RlJTI2bXNjbGtpZCUzZDdkNGEyNWM0ZTc4OTE1YjdjMTNhNGM3ZThiNGM0ZjcxJTI2bmV0d29yayUzZG8lMjZwYXJ0bmVyX2lkJTNkQ0Q5NTElMjZ0YXJnZXRfaWQlM2Rrd2QtNzgzNDA2NzYzNTY1OTAlMjZ1dG1fYWRncm91cCUzZGxjJTI1M0Q0NiUyNTNBbWFkcmlkJTI1N0NmbiUyNTNEZjMlMjU3Q2NpJTI1M0Q5MzclMjUzQXRoaW5ncyUyNTIwdG8lMjUyMGRvJTI2dXRtX2NhbXBhaWduJTNkZGMlMjUzRDIxJTI1M0FlcyUyNTdDbGMlMjUzRDQ2JTI1M0FtYWRyaWQlMjU3Q2N0JTI1M0Rjb3JlJTI1N0NsbiUyNTNEMjklMjUzQWVuJTI1N0N0YyUyNTNEYWxsJTI2dXRtX2tleXdvcmQlM2RtYWRyaWQlMjUyMGVzJTI2dXRtX21lZGl1bSUzZHBhaWRfc2VhcmNoJTI2dXRtX3F1ZXJ5JTNkbWFkcmlkJTI1MjBjaXR5JTI2dXRtX3NvdXJjZSUzZGJpbmc&rlid=7d4a25c4e78915b7c13a4c7e8b4c4f71',
    'https://www.bing.com/ck/a?!&&p=3831316e4bd0f781a30e2ec39899fd729494970d0b6a61af1ca4e421fa416661JmltdHM9MTc3Mzc5MjAwMA&ptn=3&ver=2&hsh=4&fclid=016b5505-6406-6c17-3c90-4225650b6d26&psq=madrid+city&u=a1aHR0cHM6Ly93d3cuZXNtYWRyaWQuY29tL2Vu',
    'https://www.bing.com/ck/a?!&&p=b51a6375fa3521a204578c2b2a348249defd713957b38c2c5eb05c689e2c8398JmltdHM9MTc3Mzc5MjAwMA&ptn=3&ver=2&hsh=4&fclid=016b5505-6406-6c17-3c90-4225650b6d26&psq=madrid+city&u=a1aHR0cHM6Ly93d3cuc3BhaW4uaW5mby9lbi9kZXN0aW5hdGlvbi9tYWRyaWQv',
    'https://www.bing.com/ck/a?!&&p=c738ef59341552584c067cb02700ebc57dcba1c02f84e79c0c0bdd123feb9dc0JmltdHM9MTc3Mzc5MjAwMA&ptn=3&ver=2&hsh=4&fclid=016b5505-6406-6c17-3c90-4225650b6d26&psq=madrid+city&u=a1aHR0cHM6Ly93d3cuYnJpdGFubmljYS5jb20vcGxhY2UvTWFkcmlk',
    'https://beautiful-soup-4.readthedocs.io/en/latest/',
    'https://www.bing.com/ck/a?!&&p=8100ebe93e9ef768556f1b016ca4466f532f748f59c7ed76cfb9cc5a6eb8c746JmltdHM9MTc3Mzc5MjAwMA&ptn=3&ver=2&hsh=4&fclid=016b5505-6406-6c17-3c90-4225650b6d26&psq=madrid+city&u=a1aHR0cHM6Ly93d3cudHJpcGFkdmlzb3IuY29tL1RvdXJpc20tZzE4NzUxNC1NYWRyaWQtVmFjYXRpb25zLmh0bWw',
    'https://www.bing.com/ck/a?!&&p=016499f74e36e7672e99b0814635188b069209655d7663f0b4ccda568d1ea7fdJmltdHM9MTc3Mzc5MjAwMA&ptn=3&ver=2&hsh=4&fclid=016b5505-6406-6c17-3c90-4225650b6d26&psq=madrid+city&u=a1aHR0cHM6Ly93d3cuZWFydGh0cmVra2Vycy5jb20vYmVzdC10aGluZ3MtdG8tZG8taW4tbWFkcmlkLw',
    'https://www.bing.com/ck/a?!&&p=da13ac904ff0e786eb439e219c8269fa15861b6b55cb94be8fcef86848b9824aJmltdHM9MTc3Mzc5MjAwMA&ptn=3&ver=2&hsh=4&fclid=016b5505-6406-6c17-3c90-4225650b6d26&psq=city+vs+Madrid&u=a1aHR0cHM6Ly93d3cub3V0bG9va2luZGlhLmNvbS9zcG9ydHMvZm9vdGJhbGwvbWFuY2hlc3Rlci1jaXR5LXZzLXJlYWwtbWFkcmlkLWxpdmUtc2NvcmUtdWVmYS1jaGFtcGlvbnMtbGVhZ3VlLTIwMjUtMjYtcm91bmQtb2YtMTYtc2Vjb25kLWxlZy11cGRhdGVzLWhpZ2hsaWdodHMtZXRpaGFkLXN0YWRpdW0',
    'https://www.bing.com/ck/a?!&&p=df267b98e05ddeef27c95be589b144e1e53602a1c0633657059d29b7e12ce833JmltdHM9MTc3Mzc5MjAwMA&ptn=3&ver=2&hsh=4&fclid=016b5505-6406-6c17-3c90-4225650b6d26&psq=city+vs+Madrid&u=a1aHR0cHM6Ly93d3cuZXNwbi5jb20vc29jY2VyL3N0b3J5L18vaWQvNDgyMzI0MjYvbWFuLWNpdHktdnMtcmVhbC1tYWRyaWQtbGl2ZS1sYXRlc3QtdXBkYXRlcy1jaGFtcGlvbnMtbGVhZ3VlLXJvMTYtc2Vjb25kLWxlZw',
    'https://www.bing.com/ck/a?!&&p=b058601323f3d3c58e0cb5c51c459fca41b2084013b70a4630daa567443a7672JmltdHM9MTc3Mzc5MjAwMA&ptn=3&ver=2&hsh=4&fclid=016b5505-6406-6c17-3c90-4225650b6d26&psq=city+vs+Madrid&u=a1aHR0cHM6Ly93d3cuYmJjLmNvLnVrL3Nwb3J0L2Zvb3RiYWxsL2xpdmUvY2plbjh3azJldjV0'
]

loop = asyncio.get_event_loop()

#6. Exception handling
async def fetch_url(session,url):
    '''
        Returns the exception wrapped task for given url
    '''
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()
    except aiohttp.ClientConnectionError:
        print(f"Error: Cannot connect to {url}")
        return None
    except aiohttp.ConnectionTimeoutError:
        print(f"Timeout for {url}")
        return None
    except Exception as e:
        print(e)
        return None
        
def get_tasks(session):
    '''
        Adds the list of tasks to the event loop.
        Takes in aiohttp.ClientSession object as 
        session.get(url) is the task to perform.
        Returns the tasks list.
    '''
    tasks = []
    for url in urls:
        tasks.append(
            loop.create_task(fetch_url(session,url))
        )
    return tasks

async def fetch_urls():
    '''
        An async function to fetch all the urls
        concurrently. Here, we will just run the 
        tasks we get from get_tasks function.
        This speeds up the execution as we only
        need to wait for the result from the
        tasks that are already added onto the
        event loop by get_tasks().
        Returns html-code for each url.
    '''
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks) #concurrent execution
        inner_soup = []
        for response in responses:
            if response is not None:
                inner_soup.append(
                    BeautifulSoup(response,'html.parser')
                )
    return inner_soup
    
# async def fetch_urls(urls):
#     '''
#         An async function to fetch all the urls
#         from the passed list concurrently.
#         This version is a slow one because we are adding
#         tasks one by one onto the event loop.
#     '''
#     async with aiohttp.ClientSession() as session:
#         for url in urls:
#             response = await session.get(url)
#             print(await response.text())

# def fetch_urls(urls):
#     '''
#         A sync function to fetch all the urls
#         from the passed list one after another.
#     '''
#     for url in urls:
#         response = requests.get(url)
#         print(response.text) 

# start = time.time()

# loop.run_until_complete(fetch_urls(urls))
# fetch_urls(urls)
# loop.run_until_complete(fetch_urls())

# print(f"\nTime taken: {time.time() - start} seconds\n")

#1. fetch data
inner_soups = loop.run_until_complete(fetch_urls()) 
data = []

#2,3. parsing html and extracting title and desc
for soup in inner_soups:
    curr = []
    curr.append(soup.title.string)
    curr.append("None")
    if soup.meta:
        metas = soup.find_all('meta')
        for meta in metas:
            if 'name' in meta.attrs and meta['name'] == 'description':
                curr[-1] = meta['content']
    data.append(curr)

#4. saving results to csv
f = open('task17data.txt','w')
csv.writer(f).writerows(data)

loop.close()