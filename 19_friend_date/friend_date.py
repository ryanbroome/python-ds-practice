def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    elmo = ('Elmo', 5, ['hugging', 'being nice'])
    sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
    gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

    if a == 'elmo':
        a = elmo
    if b == 'elmo':
        b = elmo
    if a == 'sauron':
        a = sauron
    if b == 'sauron':
        b = sauron
    if a == 'gandalf':
        a = gandalf
    if b == 'gandalf':
        b = gandalf
    
    has_true = []

    for hobby in a[2]:
        has_true.append(b[2].count(hobby) > 0)
    
    if has_true.count(True) > 0:
        return True
    else: return False