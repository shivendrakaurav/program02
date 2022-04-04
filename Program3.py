import re
import time
import random
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

def random_email_generator():
    var = ""
    for x in range(random.randint(0,40)):
        var = var + chr((list(range(65,91))+list(range(48,58)) + list(range(97,123)) +[95] + [45] + [46])[random.randint(0,63)])
    return var

def removing_duplicity(var):
    L =[]
    for x in var:
        count = 0
        for y in L:
            if y.upper() ==x.upper():
                count+=1
        if count ==0:
            L.append(x)
    return L

start = time.time()
with open("L1.txt", "w") as f:
    for i in range(60000):
        email = random_email_generator() + "@" + random_email_generator() + "." + random_email_generator()
        f.write(email + "\n")

# with open("L2.txt", "w") as f:
#     for i in range(10):
#         email = random_email_generator() + "@" + random_email_generator() + "." + random_email_generator()
#         f.write(email + "\n")

emails = []
with open("L1.txt",'r') as f:
    for email in f.readlines():
        if checking_email(email.strip()):
            emails.append(email.strip())
emails = removing_duplicity(emails)
end = time.time()
print(len(emails))
print(end - start)
# emails1 = []
# with open("L2.txt",'r') as f:
#     for email in f.readlines():
#         if checking_email1(email1.strip()):
#             emails1.append(email1.strip())
# print(emails1)
# emails1 = removing_duplicity(emails1)





