



def union(l1_file, l2_file):
    """Performs union operation on list1 and list2
    py:function::

    Args:
        list1,list2(list) : lists on which union operation is performed

    Returns:
        dictionary: unique emails by adding two lists
    """
    key_value_emails = {}
    for key in l1_file + l2_file:
        key_value_emails[key] = 1
    return key_value_emails


def intersection(l1_file, l2_file):
    """Performs intersection operation on list1, list2
    py:function::

    Args:
        list1,list2(list) : lists on which intersection operation is performed

    Returns:
        dictionary: emails common in both lists
    """
    key_value = {}
    key_value_l1 = {}
    for email in l2_file:
        key_value_l1[email] = 1
    for key in l1_file:
        if key in key_value_l1.keys():
            key_value[key] =1
    return key_value

def minus(l1_file, l2_file):
    """Performs minus operation of list1 from list2
    py:function::

    Args:
        list1,list2(list): lists on which intersection is performed

    Return:
        dictionary: emails present in only list1
    """
    key_value_email={}
    key_value = {}
    for value in l2_file:
        key_value[value] = 1
    for key in l1_file:
        if key not in key_value.keys():
            key_value_email[key] =1
    return key_value_email