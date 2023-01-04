def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """ 
    # phrase[-1:]

    rev_phrase = phrase[: -(len(phrase)): -1]
    return rev_phrase + phrase[0]