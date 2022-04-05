import re
import time
import sys
def checking_special_chr_space(var):
    for y in var:
        if len(re.findall("[0-9@a-zA-Z._-]", y)) == 0:
            return False
    return True


def checking_first_last_digit(var):
    if len(re.findall("[0-9a-zA-Z]", var[0])) ==0 or len(re.findall("[0-9a-zA-Z]", var[-1])) ==0:
        return False
    else:
        return True

def checking_gmailsymbols(var):
    if "." in var and "@" in var and var.count("@")==1:
        return True
    else:
        return False

def checking_char_around_specialchar(var):
    if  var[var.rfind("@")-1] in "._-" or var[var.rfind("@")+1] in "._-" :
        return False
    elif var[var.rfind(".") - 1] in "._-" or var[var.rfind(".") + 1] in "._-":
        return False
    else:
        return True

def checking_consecutive_specialchar(var):
    for y in range(len(var)-1):
        if  var[y] in ".-_" and  var[y+1] in ".-_":
            return False
    return True


def checking_email(var):
    if checking_special_chr_space(var) and checking_first_last_digit(var):
        if checking_gmailsymbols(var) and checking_char_around_specialchar(var):
            if checking_consecutive_specialchar(var):
                return True
    return False

def adding_email_to_hashfunction(email,emails):
    if email.upper() in emails.values():
        return False
    else:
        return True

def main_function(y):
    with open(y, 'r') as f:
        emails = {}
        i = 0
        for email in f.readlines():
            if checking_email(email.strip()):
                if adding_email_to_hashfunction(email, emails):
                    emails[i] = email.upper()
                    i += 1
    return emails

def minus_function(list1,list2,y):
    L=[]
    for value in list1.values():
        if value not in list2.values():
            L.append(value)
    for value in list2.values():
        if value not in list1.values():
            L.append(value)

    with open(y, "w") as f:
        for i in L:
            f.write(i + "\n")
    return L


# main function
start = time.time()
list1 = main_function(sys.argv[1])
list2 = main_function(sys.argv[2])
list3 = minus_function(list1,list2,sys.argv[3])

end = time.time()
print(f"L1.txt: {len(list1)} emails, L2.txt: {len(list2)} emails, R.txt: {len(list3)} emails ; Time Taken: {end - start} seconds")