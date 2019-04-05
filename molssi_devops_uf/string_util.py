"""
string_math.py
A sample repository for the MOLSSI workshop at UF.

Some string functions.
"""


def title_case(sentence):
    """
    make the string title cased

    Parameters
    ----------
    sentence : string
        The string to make the title case of

    Returns
    ----------
    ret : string
        Title cased string

    Example
    ----------
    >>> title_case('ThiS is A StrinG')
        'This Is A String'
    """

    # check the input is string
    if not isinstance(sentence, str):
        raise TypeError('Invalid input %s - Input must be type string' % (sentence))

    if len(sentence) == 0:
        raise ValueError('Cannot apply title_case to empty string')

    ret = sentence[0].upper()

    for i in range(1, len(sentence)):
        if sentence[i - 1] == ' ':
            ret += sentence[i].upper()

        else:
            ret += sentence[i].lower()

    return ret
