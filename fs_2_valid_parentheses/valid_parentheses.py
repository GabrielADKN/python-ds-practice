def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    climb = 0
    
    for char in parens:
        if char == "(":
            climb += 1
        elif char == ")":
            climb -= 1
    
        if climb < 0:
            return False
    
    return climb == 0