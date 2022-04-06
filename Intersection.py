import re
import time
import sys


def checking_email_except_repetitive_specialchar(string):

    pattern = '^[a-zA-Z0-9][-a-zA-Z0-9._]*[a-zA-Z0-9]@[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]\.[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]$'
    pattern2 = '^[a-zA-Z0-9]([-a-zA-Z0-9._][a-zA-Z0-9])*@[a-zA-Z0-9]([a-zA-Z0-9-][a-zA-Z0-9])*\.[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]$'
    if re.match(pattern, string) or re.match(pattern2, string):
        return True
    else:
        return False

def checking_consecutive_specialchar(char):
    for y in range(len(char)-1):
        if  char[y] in ".-_" and  char[y+1] in ".-_":
            return False
    return True

def checking_email(var):
    if checking_email_except_repetitive_specialchar(var):
        if checking_consecutive_specialchar(var):
            return True
    else:
        return False

def main_function(y):
    with open(y, 'r') as f:
        emails = {}
        for email in f.readlines():
            if checking_email(email.strip()):
                emails[email.upper()] = 1
    return emails

def intersection_function(list1,list2,y):
    list = []
    for key in list1.keys():
        if key in list2:
            list.append(key)

    with open(y, "w") as f:
        for value in list:
            f.write(value + "\n")
    return list


# main function
start = time.time()
list1 = main_function(sys.argv[1])
list2 = main_function(sys.argv[2])
list3 = intersection_function(list1,list2,sys.argv[3])

end = time.time()
print(f"L1.txt: {len(list1)} emails, L2.txt: {len(list2)} emails, R.txt: {len(list3)} emails ; Time Taken: {end - start} seconds")