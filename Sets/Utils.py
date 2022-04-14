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
            if email_checker(email.strip()):
                file.append(email.upper())
    return file


def write_file(key_value_result, file_name ):
    
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


def email_checker_except_repetitive_specialchar(string):
    
    """check whether string in coherence with regex funcion or not
    py:function::

    Args:
        string(string) : the string to check

    Returns:
        bool: "True" if string matches with any of the regex function
    """
    
    pattern_1 = '^[a-zA-Z0-9][-a-zA-Z0-9._]*[a-zA-Z0-9]@[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]\.[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z]$'
    pattern_2 = '^[a-zA-Z0-9]([-a-zA-Z0-9._][a-zA-Z0-9])*@[a-zA-Z0-9]([a-zA-Z0-9-][a-zA-Z0-9])*\.[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z]$'
    if re.match(pattern_1, string) or re.match(pattern_2, string):
        return True
    else:
        return False

def checking_consecutive_specialchar(email_string):
    
    """ Check whether email_string has consecutive special charachter or not
    py:function::

    Args:
        email_string(str): string to check

    Returns:
        bool: "True" if email_string has no consecutive special charachter
    """
    
    for postion_of_char in range(len(email_string) - 1):
        if  email_string[postion_of_char] in ".-_" and  email_string[postion_of_char + 1] in ".-_":
            return False
    return True


def email_checker(email_string):
    
    """Checks whether email_string is valid or not
    py:function::

    Args:
        email_string(str): string to check

    Returns:
        bool: "True" if email is valid
    """
    
    if email_checker_except_repetitive_specialchar(email_string):
        if checking_consecutive_specialchar(email_string):
            return True
    else:
        return False










