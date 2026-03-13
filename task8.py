'''
    Exercise 8: Dataclasses with Validation         
    Topics Covered: Dataclasses, Exception Handling

    Create a `@dataclass` for `Employee` with:
    - Fields: id, name, email, salary, department, hire_date
    - Post-init validation (email format, salary > 0, valid department)
    - Custom `__str__` for pretty printing
    - Frozen dataclass option for immutable records
    - Ordering based on salary
    - Factory method to create from dictionary
'''
from dataclasses import dataclass, fields
import datetime as dt
import re

@dataclass
class Employee:
    '''
        A dataclass for employee with fields id,name,email,salary,department and hire_date
    '''
    id: str
    name: str
    email: str
    salary: int
    department: str
    hire_date: dt.date
    
    def __post_init__(self):
        '''
            Post initialization of field values
        '''
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        depts = ('Engineering','Sales','Marketing')
        if not re.match(email_regex,self.email):
            raise ValueError("Invalid email")
        if not self.salary > 0:
            raise ValueError("Salary must be greater than 0")
        if not self.department in depts:
            raise ValueError(f"Department must be in {depts}")
        
    def __str__(self):
        '''
            Pretty printing of values
        '''
        print("Employee details: ")
        for field in fields(self):
            val = getattr(self,field.name)
            print(f"{field.name}: {val}")
    
@dataclass(frozen=True)
class FrozenEmployee:
    '''
        A dataclass for employee with fields id,name,email,salary,department and hire_date
    '''
    id: str
    name: str
    email: str
    salary: int
    department: str
    hire_date: dt.date
    
    def __post_init__(self):
        '''
            Post initialization of field values
        '''
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        depts = ('Engineering','Sales','Marketing')
        if not re.match(email_regex,self.email):
            raise ValueError("Invalid email")
        if not self.salary > 0:
            raise ValueError("Salary must be greater than 0")
        if not self.department in depts:
            raise ValueError(f"Department must be in {depts}")
        
    def __str__(self):
        '''
            Pretty printing of values
        '''
        print("Employee details: ")
        for field in fields(self):
            val = getattr(self,field.name)
            print(f"{field.name}: {val}")