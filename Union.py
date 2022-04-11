import re
import time
import sys
import os

def checking_email_except_repetitive_specialchar(char):
    """check whether email is correct or not and do not check special repetitive charachter
    py:function::

    Args:
        char(string) : the string to check

    Returns:
        bool: "True" if email is correct

    """

    pattern = '^[a-zA-Z0-9][-a-zA-Z0-9._]*[a-zA-Z0-9]@[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]\.[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]$'
    pattern2 = '^[a-zA-Z0-9]([-a-zA-Z0-9._][a-zA-Z0-9])*@[a-zA-Z0-9]([a-zA-Z0-9-][a-zA-Z0-9])*\.[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]$'
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

def read_file(y):
    """ reading emails from a file and adding correct email to a list
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

def union(list1,list2):
    """Performs union operation on two lists
    py:function:

    Args:
        list1,lits2(list) : lists to perform union operation

    Return:
        dictionary: returns emails in dict after performing union operation
    """
    emails = {}
    for value in list1 + list2:
        emails[value] = 1
    return emails

def write_file(result):
    """Write the result of union function in

    """
    with open(ret_file, "w") as f:
        for key in result.keys():
            f.write(key + "\n")

def validate_args(y):
    list1 = y[1]
    list2 = y[2]
    list3 = y[3]
    if ((os.path.exists(y[1]) and os.stat(y[1]).st_size >0)):
        pass
        if ((os.path.exists(y[2]) and os.stat(y[2]).st_size > 0)):
            if os.path.exists(y[3]) and os.stat(y[3]).st_size ==0:
                return y[1],y[2],y[3]
            else:
                list3 = input("enter the correct file3 name>")
                return validate_args(["",list1,list2,list3])
        else:
            list2 = input("enter the correct file2 name>")
            return validate_args(["", list1, list2, list3])
    else:
        list1= input("enter the correct file1 name>")
        return validate_args(["", list1, list2, list3])

# main function
if __name__ =="__main__":
    l1_file, l2_file, ret_file = validate_args(sys.argv)
    start = time.time()
    l1 = read_file(l1_file)
    l2 = read_file(l2_file)
    result = union(l1,l2,)
    write_file(result)

    end = time.time()
    print(f"{l1_file}: {len(l1)} emails, {l2_file}: {len(l2)} emails, {sys.argv[3]}: {len(result)} emails; Time Taken: {end - start} seconds")

