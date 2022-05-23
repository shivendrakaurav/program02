import re
import time
import sys
import os
from pre_defined_function import checking_email,checking_email_except_repetitive_specialchar,checking_consecutive_specialchar

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

def union(list1,list2):
    """Performs union operation on two lists
    py:function:

    Args:
        list1,lits2(list) : lists to perform union operation

    Return:
        dictionary: returns emails inside dictionary
    """
    emails = {}
    for value in list1 + list2:
        emails[value] = 1
    return emails

def write_file(result):
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
        for x in range(1, 4):
            if not (os.path.exists(y[x])):
                raise Exception(f"{y[x]} file does not exist")
            if os.stat(y[x]).st_size == 0 and x != 3:
                raise Exception(f"{y[x]} file is empty")

        if os.stat(y[3]).st_size != 0:
            raise Exception(f"{y[3]} is not empty")
        return y[1], y[2], y[3]

    else:
        raise Exception("Usage: python Union.py <in_file1> <in_file2> <result_file>")

# main function
if __name__ =="__main__":
    try:
        start = time.time()
        l1_file, l2_file, ret_file = validate_args(sys.argv)
        l1 = read_file(l1_file)
        l2 = read_file(l2_file)
        result = union(l1,l2)
        write_file(result)

        end = time.time()
        print(f"Output: {l1_file}: {len(l1)} emails, {l2_file}: {len(l2)} emails, {sys.argv[3]}: {len(result)} emails; Time Taken: {end - start} seconds")

    except Exception as e1:
        print("Generic error: {0}".format(e1))

