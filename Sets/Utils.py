import re
import time
import sys
import os


def read_file(y):
    """ checking correctness of email
    py:function::

    Args:
        y(file name) : file to check emails

    Returns:
        list : returns correct emails in list format
    """
    with open(y, 'r') as f:
        emails = []
        for email in f.readlines():
            if checking_email(email.strip()):
                emails.append(email.upper())
    return emails


def write_file(result,ret_file):
    """Write the result of union function
     py:function::

     Args:
         result(dictionary) : dictionary to write in ret_file

    Return:
        None : Does not writing anything
    """
    with open(ret_file, "w") as f:
        for key in result.keys():
            f.write(key + "\n")


def validate_args(y):
    """checks whether args entered are correct or not
    py:function::

    Args:
        y(list) : args in list format

    Return:
        tuple : return list if argv entered is right

    """
    if (len(sys.argv) == 4):
        for x in range(1, 3):
            if not (os.path.exists(y[x])):
                raise Exception(f"{y[x]} file does not exist")
            if os.stat(y[x]).st_size == 0 :
                raise Exception(f"{y[x]} file is empty")

        # if os.stat(y[3]).st_size != 0:
        #     raise Exception(f"{y[3]} is not empty")
        return y[1], y[2], y[3]

    else:
        raise Exception("Usage: python Union.py <in_file1> <in_file2> <result_file>")


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










