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
        dictionary: returns emails in dictionary format
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
    if ((os.path.exists(y[1]) and os.stat(y[1]).st_size >0)) and ((os.path.exists(y[2]) and os.stat(y[2]).st_size > 0)) and (os.path.exists(y[3]) and os.stat(y[3]).st_size ==0):
            return y[1],y[2],y[3]
    else:
         raise Exception("File not found ")

# main function
try:
    if __name__ =="__main__":
        start = time.time()
        l1_file, l2_file, ret_file = validate_args(sys.argv)
        l1 = read_file(l1_file)
        l2 = read_file(l2_file)
        result = union(l1,l2,)
        write_file(result)

        end = time.time()
        print(f"{l1_file}: {len(l1)} emails, {l2_file}: {len(l2)} emails, {sys.argv[3]}: {len(result)} emails; Time Taken: {end - start} seconds")

except Exception as e1:
    print("Generic error: {0}".format(e1))

