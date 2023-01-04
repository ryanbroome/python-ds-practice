def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    ans = 1
    even_nums =  [num for num in nums if num % 2 ==0]
    for num in even_nums:
        print(f'starting number is {num}, multiplied by {ans} ==>> {num*ans}')
        ans = ans * num
    print(f'All the evens multiplied == {ans}')
    return ans
        
  

