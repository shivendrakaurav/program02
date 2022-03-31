
#1(divisibility of 2 )
def is_divi2(y):
    return y[-1] in ("0", "2", "4", "6", "8")

#2(divisibility of 3)
def is_divi3(x):
    x = sum(int(a) for a in str(x))
    if x in(3,6,9):
        return True
    if x < 10:
        return False
    return is_divi3(x)


#3(divisibility of 4)
def is_divi4(a):
    if (int(a[len(a) - 2]) in (0, 2, 4, 6, 8) and int(a[len(a) - 1]) in (0, 4, 8)):
        return True
    if (int(a[len(a) - 2]) in (1, 3, 5, 7, 9) and int(a[len(a) - 1]) in (2, 6)):
        return True
    return False

#4(divisibility of 5)
def is_divi5(a):
    return (int(a[-1]) in (0, 5))


#5(divisibility of 6)
def is_divi6(a):
    return (2 in (a) and 3 in (a))

#6(divisibility of 7)
def is_divi7(a):
    a = int(a)
    if (a in (7, 49)):
        return True
    if a < 10:
        return False
    a = int(str(a)[0:-1]) + int(str(a)[-1]) * 5
    return is_divi7(a)

#7(divisibility of 8)
def is_divi8(a):
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
def is_divi9(a):
    a = sum(int(x) for x in str(a))
    if a == 9:
        return True
    if a <10:
         return False
    return is_divi9(a)

def is_divisible_by(y):
    a = []
    i=1
    for y in  (is_divi2(y),is_divi3(y), is_divi4(y),is_divi5(y),is_divi6(a),is_divi7(y),is_divi8(y),is_divi9(y)) :
        i+=1
        if y:
            a.append(i)
    return a

git
# Main Program starts here
input = input("Enter the number >")
input = input.split(",")

for y in input:
    L=[]
    L = is_divisible_by(y)

    if (len(L) > 0):
        print("{}: is divisible by {}".format(y, ",".join(list(map(str, L)))))
    else:
        print("{}: is not divisible".format(y))





