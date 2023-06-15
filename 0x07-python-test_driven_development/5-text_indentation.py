#!/usr/bin/python3
'''Print text with a newline after '.', '?', and ':'
'''


def text_indentation(text):
    '''Parse the string input text where the characters
    '.', '?', or ':' appear and print to stdout
    Args:
        1. text (str): the input text to parse
    Raises:
        1. TypeError: if the text is not a string
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
