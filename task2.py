'''
    Exercise 2: Nested Dictionary Operations
'''
    
def flatten_emp_dict(emp_data,emp_list):
    '''
        Recursive function that flattens the given employee dict and modifies the list provided in arg to contain all the employees
    '''
    
    if emp_data is None:
        return
    
    for internal_value in emp_data.values():
        if type(internal_value) == dict:
            flatten_emp_dict(internal_value,emp_list)
        else:
            for v in internal_value:
                emp_list.append(v)
                
def count_per_dept (emp_data):
    '''
        Counts the no of employees per department and returns a dictionary of the same
        Uses the flatten_emp_dict function to get the list per department and then counts the total
    '''
    dept_wise_count = {}
    for key, value in emp_data.items():
        emp_lst = []
        flatten_emp_dict(value,emp_lst)
        dept_wise_count[key] = len(emp_lst)
        
    return dept_wise_count

def find_emp_team (emp_name,emp_data):
    '''
        Takes in the employee name and prints the corresponding team name
    '''
    for internal_key, internal_value in emp_data.items():
        if type(internal_value) == dict:
            emp_team = find_emp_team(emp_name,internal_value)
            if emp_team:
                return emp_team
        else:
            if emp_name in internal_value:
                return internal_key
    
    return None

def reverse_mapping(emp_data):
    '''
        Takes in the company data and returns a reverse dict in the format `{employee: [department, team]}`
    '''
    # reverse_dict = {[dep,team] for dep,team in emp_data.items()}
    # return reverse_dict
    pass
    
if __name__ == "__main__":
    company = {
        "Engineering": {
            "Backend": ["Alice", "Bob", "Charlie"],
            "Frontend": ["David", "Eve"],
            "DevOps": ["Frank"]
        },
        "Sales": {
            "North": ["Grace", "Henry"],
            "South": ["Ivy"]
        }
    }
    
    emp_list = []
    flatten_emp_dict(company,emp_list) #1. Flatten
    print(f"Employee list: {emp_list}")
    
    dept_wise_count = count_per_dept(company) #2. Count per department
    print("\nEmployee count per department:")
    for key, value in dept_wise_count.items():
        print(f"{key}: {value}")
        
    emp_name = input("\nEnter the name of the employee to find: ")
    emp_team = find_emp_team(emp_name,company) #3. Find emp team
    if emp_team is None:
        print("Employee not found")
    else:
        print(f"Employee found in {emp_team} team")
        
    reverse_mapping_dict = reverse_mapping(company) #4. Reverse mapping
    print (reverse_mapping_dict)