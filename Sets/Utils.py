import re
import sys
import os


def read_file(file_name):
    """ open file, checks valid email and add valid email to list.
    py:function::

    Args:
        file_name(str) : file name from which emails are validated

    Returns:
        list :  valid emails
    """
    with open(file_name, 'r') as f:
        file = []
        for email in f.readlines():
            if checking_email(email.strip()):
                file.append(email.upper())
    return file


def write_file(key_value_result, file_name):
    """Opens file_name and write result(dictionary) keys inside it
     py:function::

     Args:
         key_value_result(dictionary) : file on which result values are written

    Return:
        None : Does not give any output
    """
    with open(file_name, "w") as f:
        for key in key_value_result.keys():
            f.write(key + "\n")


def validate_args(argv_list):
    """checks whether argv_list having 4 values or not, checks whether 2nd and 3rd argv_list values exists and not null.
    py:function::

    Args:
        argv_list(list) : list to check for validity

    Return:
        tuple : if argv_list is correct

    """
    if (len(argv_list) == 4):
        for x in range(1, 3):
            if not (os.path.exists(argv_list[x])):
                raise Exception(f"{argv_list[x]} file does not exist")
            if os.stat(argv_list[x]).st_size == 0 :
                raise Exception(f"{argv_list[x]} file is empty")

        # if os.stat(y[3]).st_size != 0:
        #     raise Exception(f"{y[3]} is not empty")
        return argv_list[1], argv_list[2], argv_list[3]

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










