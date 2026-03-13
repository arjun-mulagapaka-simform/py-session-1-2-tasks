'''
    Exercise 13: Collections Module - Counter & defaultdict
    Topics Covered: Collections

    Given a text file:
    1. Use `Counter` to find top 10 most common words
    2. Use `defaultdict(list)` to group words by their first letter
    3. Use `deque` to implement a rotating buffer (max size 100)
    4. Use `namedtuple` to create structured log entries
'''

from collections import Counter,defaultdict,deque,namedtuple

if __name__ == "__main__":
    with open('task13txtfile.txt','r') as f:
        words = f.read().split(" ")
        
        words = [word.strip() for word in words 
                 if (not word.isnumeric() and not '-' in word and not ':' in word)] #removing numeric values since they are not words
        
        #1. top 10 common words
        most_common_words = Counter(words).most_common(10) #counter first creates a key:value pair like 'hello:3' and then we return the top 10
        print("10 most common words in the file are:")
        print(*most_common_words)
        
        #2. groups based on first letter
        f_letter_groups = defaultdict(set)
        for word in words:
            f_letter_groups[word[0]].add(word)
            
        print("\nGroups based on first letter are:")
        for k,v in f_letter_groups.items():
            print(k,":",v)
        
        #3. rotating buffer of max_len=100 which stores letters from the file
        f.seek(0,0) #repositioning read head to start
        
        letter_rotating_buffer = deque(maxlen=100) #maxlen automatically creates a rotating buffer for you
        
        for letter in f.read():
            if not letter.isspace():
                letter_rotating_buffer.append(letter)
        
        print("\nElements of the rotating buffer are:")
        print(*letter_rotating_buffer)
        
        #4. namedtuple with structured log entries
        f.seek(0,0) #repositioning read head to start
        
        log = namedtuple('log',
                         ['loglevel','message','timestamp']) #log in the format 'loglevel:<>,message:<>,timestamp:<>
        
        logs = []
        
        for line in f.readlines():
            log_data = line.split(",")
            
            logs.append(
                log(loglevel=log_data[0].strip(),message=log_data[1].strip(),timestamp=log_data[2].strip())
            )
        
        print("\nStructured logs: ")
        for i in logs:
            print(i)