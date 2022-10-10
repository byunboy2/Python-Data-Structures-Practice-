def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    lower_case_phrase = phrase.lower()
    no_space_phrase = lower_case_phrase.replace(" ","")
    reversed_string = no_space_phrase[::-1]
    return no_space_phrase == reversed_string