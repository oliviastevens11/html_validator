#!/bin/python3
# got help from QCL mentors and collaborated with students who attended with me
import re


def validate_html(html):
    '''
    This function performs a limited version of
    html validation by checking whether every opening tag has a
    corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a list of
    # html tags without any extra text;
    # then process these html tags using the balanced
    # parentheses algorithm from the class/book
    # the main difference between your code and the code from class
    # will be that you will have to keep track of not
    # just the 3 types of parentheses,
    # but arbitrary text located between the html tags
    if len(html) == 0:
        return True  # early exit
    tags = _extract_tags(html)
    if not tags:
        return False  # no valid tags (basically saying if tags == 0)
    stack = []
    balanced = True
    index = 0
    while index < len(tags) and balanced:
        tag2 = tags[index]  # puts it in a for loop
        if '/' not in tag2:
            stack.append(tag2)
        else:
            if not stack:
                balanced = False
            else:
                last = stack.pop()
                if not match(last, tag2):
                    balanced = False
        index += 1
    if balanced and not stack:
        return True
    else:
        return False


def match(firstword, secondword):
    first, second = firstword.replace('/', ""), secondword.replace('/', "")
    return first == second


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant
    to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html
    tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags_html = re.findall(r'<[^>]+>', html)
    return tags_html
    # [^>]+ means that anything can be in there
