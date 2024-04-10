def reverse(text: str) -> str:
    """
    Return the 'text' backwards.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    str
        The text written backwards.
    """

    return text[::-1]


def first_to_upper(text: str) -> str:
    """
    Changes each first character of the word to uppercase.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    str
        The modified text
    """
    pass


def count_vowels(text: str) -> int:
    """
    Counts number of vovels in the text.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    inp
        Number of vowels.
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'ą', 'Ą', 'ę', 'Ę', 'ó', 'Ó', 'y', 'Y']
    counter = 0
    for x in text:
        for y in vowels:
            if x == y: counter = counter + 1

    return counter


def sum_digits(text: str) -> int:
    """
    Finds all digitts in the text and returns its sum.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    int
        Sum of all digits in the text.
    """
    suma = 0
    for x in text:
     if x.isdigit() == True:
      suma = suma + int(x)

    return suma


def search_substr(text: str, sub: str) -> int:
    """
    Search for sub(string) in the text. Returns the position or None.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    int or None
        Position of the sub(string) or None.
    """
    if text.find(sub) == -1:
        return None
    else:
        return text.find(sub)
