def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    return_dict = {}
    for i in phrase:
        if i.lower() in vowels:
            if i.lower() in return_dict:
                return_dict[i.lower()] += 1
            else:
                return_dict[i.lower()] = 1
    return return_dict