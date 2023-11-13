def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    must_return = ""
    for char in phrase:
        if char.lower() == to_swap.lower():
            must_return += char.swapcase()
        else:
            must_return += char
    return must_return