def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    # number_compare(0, 1) 
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    elif b == a:
        return "Numbers are equal"

print(number_compare(1, 1))
print(number_compare(-1, 1))
print(number_compare(1, -2))