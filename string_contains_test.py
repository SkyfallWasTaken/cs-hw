# I know that adding "test" to the filename to test it is bad practice
# I'm not a Python programmer!

def contains(string1, string2):
    """
    Returns True if string1 contains string2
    """

    if string2 in string1:
        # string2 is in string1! Return True to signify that we found it
        return True
    else:
        # string2 is not in string1, so we return False
        return False
    
def test_contains():
    assert contains("banana", "ana") == True
    assert contains("racecar", "car") == True
    
    assert contains("cool", "test") == False
    assert contains("hello", "hi") == False