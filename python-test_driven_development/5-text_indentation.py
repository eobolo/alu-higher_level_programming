#!/usr/bin/python3
"""
a function that prints a text with 2 new lines

after each of these characters: ., ? and :

There should be no space at the beginning

or at the end of each printed line

You are not allowed to import any module
"""


def text_indentation(text):
    """
    text must be a string,

    otherwise raise a TypeError exception

    with the message text must be a string
    """
    try:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        i = 0
        new_string = ""
        while i < len(text):
            if text[i] in ['?', '.', ':']:
                new_string += text[i]
                new_string += "\n\n"
                i += 2
            else:
                new_string += text[i]
                i += 1
        return print(new_string, end="")
    except TypeError:
        raise
# text_indentation("Am I the greatest ever? \
# in the history of football. Yes you are \
# Obolo Emmanuel. How old are you: 24 I guess.")
# text_indentation("")
# text_indentation()
# text_indentation(None)
# text_indentation(246)