'''
    Exercise 1: Advanced Type Conversion & Validation
'''

def none_exception(value):
    '''
        Raises an exception if value is none otherwise False
        Wrote this function just for the sake of reusability
    '''
    if value is None:
        raise Exception('None value cannot be converted')
    return False

def safe_convert(value, target_type):
    '''
        A function to safely convert between types
        Accepts value to be converted and the target type
        Type must be in (`int`, `float`, `str`, `bool`)
        Returns a tuple in the format (success: bool, result: any, error_message: str)
    '''
    
    try:   
        match target_type.__name__:
            case 'int':
                none_exception(value)
                result = int(value)
            case 'bool':
                if type(value) == str:
                    if value.strip().lower() in ('true','1'):
                        result = True
                    else:
                        result = False
                else:
                    result = bool(value)
            case 'float':
                none_exception(value)
                result = float(value)
            case 'str':
                result = str(value)
            case _:
                raise Exception('Target type not accepted')
        
    except Exception as e:
        success = False
        result = None
        error_msg = e.args[0]
        
    else:
        success = True
        error_msg = ""
        
    finally:
        return (success, result, error_msg)
    
if __name__ == "__main__":
    assert safe_convert("123", int) == (True, 123, "")
    assert safe_convert("12.5", float) == (True, 12.5, "")
    assert safe_convert("abc", int)[0] == False
    assert safe_convert(None, str) == (True, "None", "")
    assert safe_convert("True", bool) == (True, True, "")
    assert safe_convert("False", bool) == (True, False, "")
    assert safe_convert("0", bool) == (True, False, "")
    
    assert safe_convert("", int)[0] == False
    assert safe_convert(" 10 ", int) == (True, 10, "")
    assert safe_convert("False", bool)[1] == False
    assert safe_convert(12.9, int) == (True, 12, "")
    assert safe_convert(False, int) == (True, 0, "")
    assert safe_convert("nan", float)[0] == True
    assert safe_convert("inf", float)[0] == True
    assert safe_convert(None, bool) == (True, False, "")