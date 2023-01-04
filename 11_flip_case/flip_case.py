def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    ans = []
    for char in phrase:
        print(char)
        if char == to_swap:
            char = char.swapcase()
            ans.append(char)
        elif char == to_swap.swapcase():
            char = char.swapcase()
            ans.append(char)
        elif char != to_swap or char != to_swap.swapcase():
            ans.append(char) 
        

    # new = []
    # for char in phrase:
    #     if char == to_swap:
    #         char = char.swapcase()
    #         new.append(char)
    #     if char != to_swap:
    #         new.append(char)

    return ans
    # [char.swapcase() if char == to_swap or to_swap.lower() else char  for char in phrase]
    
 
