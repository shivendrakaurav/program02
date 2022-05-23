from .Utils import email_checker

class Myset(dict):

    def __init__(self,file_name = None):
        if file_name is not None:
            self.read_file(file_name)

    def __or__(self, other):
        return self.union(other)


    def union(self,other):

        """Performs union operation on l1_list and l2_list
        py:function::

        Args:
            l1_list,l2_list(list) : lists on which union operation is performed

        Returns:
            dictionary: unique emails by adding two lists
        """

        key_value_emails = {}
        res = Myset()
        for key in self.keys():
            res[key] = 1
        for key in other.keys():
            res[key] = 1
        return res


    def intersection(self, l1_list, l2_list):

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

    def minus(self,l1_list, l2_list):

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


    def read_file(self,file_name):
        """ open file, checks valid email and add valid email to list.
        py:function::

        Args:
            file_name(str) : file name from which emails are validated

        Returns:
            list :  valid emails
        """

        with open(file_name, 'r') as f:
            file = []
            for email in f.readlines():
                if email_checker(email.strip()):
                    var = email.strip().upper()
                    self[var] = 1



    def write_file(self, file_name):
        """Opens file_name and write result(dictionary) keys inside it
         py:function::

         Args:
             key_value_result(dictionary) : file on which result values are written

        Return:
            None : Does not give any output
        """

        with open(file_name, "w") as f:
            for key in self.keys():
                f.write(key + "\n")