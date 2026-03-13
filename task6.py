'''
    Exercise 6: Static, Class, and Instance Methods
'''
import datetime as dt

class DateUtils:
    '''
        A class to provide following utility functions
            days_until,
            is_valid_date,
            is_leap_year
    '''
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    
    def days_until(self,target_date):
        '''
            Returns the (target_date - calling object's date) in no of days
        '''
        days_diff = (target_date - dt.date(self.year,self.month,self.day)).days #first calculating the difference in dates and then the no of days
        return days_diff
    
    @classmethod
    def from_string(cls,date_string,format):
        '''
            Takes in a string representation of a date and returns an instance of the class
        '''
        parsed_date = dt.datetime.strptime(date_string,format).date()
        return cls(parsed_date.year,parsed_date.month,parsed_date.day)
    
    @staticmethod
    def is_leap_year(year):
        '''
            Returns True if leap year otherwise False
        '''
        if year%4 == 0: #must be divisible by 4
            if year%100 != 0:
                return True #not divisible 100, so direct conclusion that it is a leap year
            else:
                if year%400 == 0:
                    return True #if divisible by 100, then it must also be divisible by 400 to be leap year
        return False
    
    @staticmethod
    def is_valid_date(year,month,day):
        '''
            Checks if month, day and year specified is valid or not
            Returns True if valid otherwise False
        '''
        if month in (1,3,5,7,8,10,12) and day not in range(1,32): #check if month is 31 day long and whether day is actually in the range
            return False
        elif month in (4,6,9,11) and day not in range(1,31): #check for non-31day months except Feb
            return False
        elif month == 2:
            if DateUtils.is_leap_year(year): #for Feb, check if leap year
                if day not in range(1,30): 
                    return False
            elif day not in range(1,29): #if not leap year, check range directly
                return False
        
        return True
    
if __name__ == "__main__":
    print("=== Testing DateUtils ===")
    
    # Test 1: Create from string
    date1 = DateUtils.from_string("2026-03-11", "%Y-%m-%d")
    print(f"Created date from string: {date1.year}-{date1.month}-{date1.day}")
    
    # Test 2: Check valid date
    print("Is 2024-02-29 valid?", DateUtils.is_valid_date(2024, 2, 29))  # True, leap year
    print("Is 2023-02-29 valid?", DateUtils.is_valid_date(2023, 2, 29))  # False, not leap year
    
    # Test 3: Check leap year
    print("Is 2020 a leap year?", DateUtils.is_leap_year(2020))  # True
    print("Is 2100 a leap year?", DateUtils.is_leap_year(2100))  # False
    
    # Test 4: Days until a future date
    date2 = dt.date(2026, 12, 31)
    print(f"Days until {date2.year}-{date2.month}-{date2.day}: {date1.days_until(date2)}")