from beartype import beartype

@beartype
def last_element(lst: list[int]) -> int | None:
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if lst:
        return lst[-1]
    else:
        return None