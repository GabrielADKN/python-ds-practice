def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    list_words = phrase.split()
    titleized_words = []
    for word in list_words:
        titleized_words.append(word.capitalize())
    return ' '.join(titleized_words)

