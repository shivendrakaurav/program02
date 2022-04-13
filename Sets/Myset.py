



def union(list1,list2):
    """Performs union operation on list1 and list2
    py:function::

    Args:
        list1,list2(list) : lists to perform union operation

    Return:
        dictionary: returns dictionary by adding two list
    """
    emails = {}
    for value in list1 + list2:
        emails[value] = 1
    return emails


def intersection(list1,list2):
    """Performs intersection operation on list1, list2
    py:function::

    Args:
        list1,list2(list) : lists to perform intersection operation

    Returns:
        dictionary: return emails
    """
    key_value = {}
    key_value_l1 = {}
    for x in list2:
        key_value_l1[x] = 1
    for value in list1:
        if value in key_value_l1.keys():
            key_value[value] =1
    return key_value

def minus(list1,list2):
    key_value_email={}
    key_value = {}
    for x in list2:
        key_value[x] = 1
    for value in list1:
        if value not in key_value.keys():
            key_value_email[value] =1
    return key_value_email