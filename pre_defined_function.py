
import re
import os
def checking_email_except_repetitive_specialchar(char):
    """check whether email is correct or not and do not check special repetitive charachter
    py:function::

    Args:
        char(string) : the string to check

    Returns:
        bool: "True" if email is correct

    """

    pattern = '^[a-zA-Z0-9][-a-zA-Z0-9._]*[a-zA-Z0-9]@[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]\.[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z]$'
    pattern2 = '^[a-zA-Z0-9]([-a-zA-Z0-9._][a-zA-Z0-9])*@[a-zA-Z0-9]([a-zA-Z0-9-][a-zA-Z0-9])*\.[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z]$'
    if re.match(pattern, char) or re.match(pattern2, char):
        return True
    else:
        return False

def checking_consecutive_specialchar(char):
    """ Check whether email has consecutive special charachter
    py:function::

    Args:
        char(str): string to check

    Return:
        bool: "True" if string has no consecutive special charachter

    """
    for y in range(len(char)-1):
        if  char[y] in ".-_" and  char[y+1] in ".-_":
            return False
    return True


def checking_email(var):
    """checking whether email is write or not by combining other two conditions
    py:function::

    Args:
        var(str): string to check

    Returns:
        bool: "True" if email is write

    """
    if checking_email_except_repetitive_specialchar(var):
        if checking_consecutive_specialchar(var):
            return True
    else:
        return False
