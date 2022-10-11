def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """

    count = 0
    lower_case_word = word.lower()
    return lower_case_word.count(letter)


    #for let in lower_case_word:
     #   if let == letter:
      #      count += 1
    #return count