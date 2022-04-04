
#1(divisibility of 2 )
def is_divi2(y):
    '''
    check the divisibility of "n" by 2
    Args
        n(str) : the number to check
    Returns
        bool : "True" if "n" is divisible by 2
    '''
    return y[-1] in ("0", "2", "4", "6", "8")

#2(divisibility of 3)
def is_divi3(x):
    '''
     check the divisibility of "n" by 3
    Args
        n(str) : the number to check
    Returns
        bool : "True" if "n" is divisible by 3
    '''
    if(len(x)==1):
        return x in("3","6","9")
    return is_divi3(str(sum(int(a) for a in str(x))))


#3(divisibility of 4)
def is_divi4(a):
    '''
    check the divisibility of "n" by 4
    Args
        n(str) : the number to check
    Returns
        bool : "True" if "n" is divisible by 4
    '''
    if (int(a[len(a) - 2]) in (0, 2, 4, 6, 8) and int(a[len(a) - 1]) in (0, 4, 8)):
        return True
    if (int(a[len(a) - 2]) in (1, 3, 5, 7, 9) and int(a[len(a) - 1]) in (2, 6)):
        return True
    return False

#4(divisibility of 5)
def is_divi5(a):
    '''
    check the divisibility of "n" by 5
    Args
        n(str) : the number to check
    Returns
        bool : "True" if "n" is divisible by 5
    '''
    return (int(a[-1]) in (0, 5))


#5(divisibility of 6)
def is_divi6(a):
    '''
    check the divisibility of "n" by 6 using earlier list
    Args
        L(list) : list to check
    Returns
        bool : "True" if "n" is divisible by 6 when list contains 2 and 3 inside of it.
    '''
    return (2 in (a) and 3 in (a))

#6(divisibility of 7)
def is_divi7(a):
    '''
    check the divisibility of "n" by 7
    Args
        n(str) : the number to check
    Returns
        bool : "True" if "n" is divisible by 7
    '''
    if len(a) ==1 or a == "49":
        return a in ("7", "49")
    else:
        return is_divi7(str(int(str(a)[0:-1]) + int(str(a)[-1]) * 5))

#7(divisibility of 8)
def is_divi8(a):
    '''
    check the divisibility of "n" by 8
    Args
        n(str) : the number to check
    Returns
        bool : "True" if "n" is divisible by 8
    '''
    if (len(a) > 2):
        if (int(a[-3]) in (0, 2, 4, 6, 8)):
            if (int(a[-2:]) in (8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96)):
                return True
        if (int(a[-3]) in (1, 3, 5, 7, 9)):
            if (int(a[-2:]) + 4 in (8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96)):
                return True
    if int(a) in (8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96):
        return True
    return False


#8(divisibility rule of 9)
def is_divi9(x):
    '''
    check the divisibility of "n" by 9
    Args
        n(str) : the number to check
    Returns
        bool : "True" if "n" is divisible by 9
    '''
    if len(x)==1:
        return x == "9"
    return is_divi9(str(sum(int(a) for a in str(x))))

def is_divisible_by(y):
    a = []
    i=1
    for y in  (is_divi2(y),is_divi3(y), is_divi4(y),is_divi5(y),is_divi6(a),is_divi7(y),is_divi8(y),is_divi9(y)) :
        i+=1
        if y:
            a.append(i)
    return a

def removing_negative_point_sign(var2):
    L = []
    L = [x for x in var2]
    if "." in L:
        L.remove(".")
    if "-" in L:
        L.remove("-")
    L = "".join(L)
    return L

def removing_string_using_exception(input):
    L = []
    for y in input:
        try:
            if type(float(y))==float:
                L.append(y)
        except Exception as e1:
            print("Generic error : {0}".format(e1))
    return L

# Main Program starts here
input = input("Enter the number >").split(",")
input = removing_string_using_exception(input)
for y in input:
    L=[]

    y = removing_negative_point_sign(y)
    L = is_divisible_by(y)

    if (len(L) > 0):
        print("{}: is divisible by {}".format(y, ",".join(list(map(str, L)))))
    else:
        print("{}: is not divisible".format(y))
# print(help(is_divi2))
