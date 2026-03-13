'''
    Exercise 12: Generator Pipeline - Log Processing
'''

def read_logs(filename):
    '''
        Generator function to read logs from a file
    '''
    try:
        f = open(filename)
    except FileNotFoundError as f:
        print(f)
    else:
        for line in f.readlines():
            yield line
            
def parse_logs(lines):
    '''
        Generator function which parses the logs and converts each into a dict with format: {level,message,timestamp}
    '''
    for line in lines:
            line = line.split(',')
            line_d = {'level':line[0].strip(),
                      'message':line[1].strip(),
                      'timestamp':line[2].strip()}
            yield line_d
            
def filter_errors(logs):
    '''
        Generator function which filter the logs on the condition that they are ERROR level
    '''
    for log in logs:
        if log['level'] == 'ERROR':
            yield log
    
def extract_timestamps(logs):
    '''
        Generator function which returns the timestamps from the logs
    '''
    for log in logs:
        yield log['timestamp']

if __name__ == "__main__"    :
    timestamps_of_error_logs = list(extract_timestamps(filter_errors(parse_logs(read_logs('task12logs.log'))))) #generator chaining
     
    for log in timestamps_of_error_logs:
        print(log)