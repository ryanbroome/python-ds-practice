def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    frequency = {}
    temp_val = 0
    temp_key = 0

    for num in nums:
        frequency[num] = nums.count(num)
    
    for key, value in frequency.items():
        if value > temp_val:
            temp_val = value
            temp_key = key
    return temp_key
    
