import random
def random_email_generator():
    var = ""
    for x in range(random.randint(0,40)):
        var = var + chr((list(range(65,91))+list(range(48,58)) + list(range(97,123)) +[95] + [45] + [46])[random.randint(0,63)])
    return var

with open("L1.txt", "w") as f:
    for i in range(1000000):
        email = random_email_generator() + "@" + random_email_generator() + "." + random_email_generator()
        f.write(email + "\n")