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
        emails = []
        for email in f.readlines():
            if checking_email(email.strip()):
                emails.append(email.upper())
    return emails

def union_function(list1,list2,y):
    emails = {}
    for value in list1 + list2:
        emails[value] = 1

    with open(y, "w") as f:
        for key in emails.keys():
            f.write(key + "\n")
    return emails


# main function
start = time.time()
list1 = main_function(sys.argv[1])
list2 = main_function(sys.argv[2])
list3 = union_function(list1,list2,sys.argv[3])

end = time.time()
print(f"L1.txt: {len(list1)} emails, L2.txt: {len(list2)} emails, R.txt: {len(list3)} emails; Time Taken: {end - start} seconds")
