



def union(l1_list, l2_list):

    """Performs union operation on l1_list and l2_list
    py:function::

    Args:
        l1_list,l2_list(list) : lists on which union operation is performed

    Returns:
        dictionary: unique emails by adding two lists
    """

    key_value_emails = {}
    for key in l1_list + l2_list:
        key_value_emails[key] = 1
    return key_value_emails


def intersection(l1_list, l2_list):

    """Performs intersection operation on l1_list, l2_list
    py:function::

    Args:
        l1_list,l2_list(list) : lists on which intersection operation is performed

    Returns:
        dictionary: emails common in both lists
    """

    key_value = {}
    key_value_l1 = {}
    for email in l2_list:
        key_value_l1[email] = 1
    for key in l1_list:
        if key in key_value_l1.keys():
            key_value[key] =1
    return key_value

def minus(l1_list, l2_list):

    """Performs minus operation of l1_list from l2_list
    py:function::

    Args:
        l1_list,l2_list(list): lists on which intersection is performed

    Return:
        dictionary: emails present in only list1
    """

    key_value_email={}
    key_value = {}
    for value in l2_list:
        key_value[value] = 1
    for key in l1_list:
        if key not in key_value.keys():
            key_value_email[key] =1
    return key_value_email