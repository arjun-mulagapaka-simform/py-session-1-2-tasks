'''
    Exercise 15: Advanced File Operations
'''
import shutil #for copying files
import pickle, json, csv

class With_Open:
    '''
        Context manager class with methods read_line, write_line, copy_content
        Binary file ops are implemented
    '''
    def __init__(self,filename,filemode):
        self.filename = filename
        self.filemode = filemode
    
    def __enter__(self):
        try:
            self.file = open(self.filename,self.filemode)
        except FileNotFoundError as f:
            print(f)
        except PermissionError as p:
            print(p)
        except FileExistsError as f:
            print(f)
        except Exception as e:
            print(e)
        else:
            return self
    
    def __exit__(self, exc_type, exc, tb):
        self.file.close()
    
    def read_line(self):
        '''
            Reads a single line from file
        '''
        if self.filemode not in ('r','r+','w+','a+'):
            raise Exception('Current file mode does not support readig')
        return self.file.readline()
    
    def write_line(self,text):
        '''
            Writes a single line to file
            Raise exception if filemode does not support writing
        '''
        if self.filemode not in ('w','a','r+','w+','a+','wb','ab'):
            raise Exception('Current file mode does not support writing')
        self.file.write(text+"\n")
    
    @staticmethod
    def copy_content(src,dest):
        ''' 
            A static method to copy file content from given source to dest
        '''
        try:
            shutil.copyfile(src,dest)
        except FileNotFoundError as f:
            print(f)
        except shutil.SameFileError as s:
            print(s)
        except Exception as e:
            print(e)
        
    def pickle_pick(self,data):
        '''
            Converts data object to pickle and writes to self.file
        '''
        try:
            pickle.dump(data,self.file)
        except pickle.PickleError as p:
            print(p)
        except Exception as e:
            print(e)
            
    def pickle_unpick(self):
        '''
            Unpickles pickle object from self.file and returns it
        '''
        try:
            loaded_data = pickle.load(self.file)
        except pickle.PickleError as p:
            print(p)
        except Exception as e:
            print(e)
        else:
            return loaded_data
        
    def json_dump(self,data):
        '''
            Converts data object to json format and writes to self.file
        '''
        try:
            json.dump(data,self.file)
        except Exception as e:
            print(e)
            
    def json_load(self):
        '''
            Loads json data from self.file and returns it
        '''
        try:
            loaded_data = json.load(self.file)
        except Exception as e:
            print(e)
        else:
            return loaded_data
    
    def csv_dump(self,data):
        '''
            Writes csv data to self.file
        '''
        try:
            csv.writer(self.file).writerows(data)
        except Exception as e:
            print(e)
            
    def csv_load(self):
        '''
            Gets csv reader from self.file and returns it
        '''
        try:
            loaded_data = csv.reader(self.file)
        except Exception as e:
            print(e)
        else:
            return loaded_data

# Main function to test `With_Open`
def main():
    # Prepare test files for each format: Text, Pickle, JSON, CSV

    # 1. Text file (example.txt)
    with With_Open('example.txt', 'w') as f:
        f.write_line("Hello, this is a text file!")
        f.write_line("It supports reading and writing lines.")

    # 2. Pickle file (example.pkl)
    data = {'name': 'John', 'age': 30, 'city': 'New York'}
    with With_Open('example.pkl', 'wb') as f:
        f.pickle_pick(data)

    # 3. JSON file (example.json)
    json_data = {"name": "Alice", "age": 25, "city": "Los Angeles"}
    with With_Open('example.json', 'w') as f:
        f.json_dump(json_data)

    # 4. CSV file (example.csv)
    csv_data = [["Name", "Age", "City"],
                ["Mike", 32, "Chicago"],
                ["Emma", 27, "Boston"]]
    with With_Open('example.csv', 'w') as f:
        f.csv_dump(csv_data)
    
    # Test the `With_Open` class
    print("=== Testing With_Open Class ===")
    
    # Test text file reading
    with With_Open('example.txt', 'r') as file:
        print("Reading line from example.txt:", file.read_line())
    
    # Test Pickle
    with With_Open('example.pkl', 'rb') as file:
        print("\nPickle data loaded from example.pkl:", file.pickle_unpick())
    
    # Test JSON
    with With_Open('example.json', 'r') as file:
        print("\nJSON data loaded from example.json:", file.json_load())
    
    # Test CSV
    with With_Open('example.csv', 'r') as file:
        print("\nCSV data loaded from example.csv:")
        for row in file.csv_load():
            print(row)
    
    # Test copying file content
    With_Open.copy_content('example.txt', 'example_copy.txt')
    print("\nexample_copy.txt created as a copy of example.txt")

if __name__ == "__main__":
    main()