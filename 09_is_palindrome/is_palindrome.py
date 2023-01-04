def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
#============================================WORKING CODE
# REMOVE ANY SPACES OUT OF STRING
    phrase = [char for char in phrase if char != " "]
    rev_phrase = phrase[::-1]
# GET LENGTH AND LAST INDEX OF PHRASE
    length = len(phrase)
    last_index = length - 1
# USE LENGTH TO CALCULATE THE HALF LENGTH OF PHRASE IF ODD ADD ONE 
    if length % 2 == 0:
        half_length = length/2
        half_length = int(half_length)
    elif length % 2 != 0:
        half_length = (length + 1) / 2
        half_length = int(half_length)
    #CREATE LIST AND REVERSE LIST 
    char_list = [char.lower().strip() for char in phrase]
    rev_char_list = [char.lower().strip() for char in phrase[last_index: :-1 ]]
#============================================WORKING CODE

#============================================WORKING CODE
#COMPARE FIRST HALF OF CHAR LIST TO FIRST HALF OF REVERSE CHAR LIST
    if char_list[:half_length] == rev_char_list[:half_length]:
        
        return True

    elif char_list[:half_length] != rev_char_list[:half_length]:
        
        return False
#============================================WORKING CODE

    