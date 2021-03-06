# Node list is
# None or
# Node(value, rest), where rest is the rest of the list
class Node:
    def __init__(self, value, rest):
        self.value = value
        self.rest = rest
    def __eq__(self, other):
        return ((type(other) == Node)
          and self.value == other.value
          and self.rest == other.rest
        )
    def __repr__(self):
        return ("Node({!r}, {!r})".format(self.value, self.rest))

# a StrList is one of
# - None, or
# - Node(string, StrList)

# StrList -> string
# Returns first (as determined by Python compare) string in StrList
# If StrList is empty (None), return None
# Must be implemented recursively
def first_string(strlist, min = ""):
    if not strlist:
        return None
    if strlist.rest == None:
        return min
    if strlist.value < strlist.rest.value:
        return first_string(strlist.rest, strlist.value)
    else:
        return first_string(strlist.rest, strlist.rest.value)


# StrList -> (StrList, StrList, StrList)
# Returns a tuple with 3 new StrLists,
# the first one with strings from the input list that start with a vowel,
# the second with strings from the input list that start with a consonant,
# the third with strings that don't start with an alpha character
# Must be implemented recursively
def split_list(strlist, r_tuple=(Node(None,None),Node(None,None),Node(None,None)) ):
    r_list = list(r_tuple)
    if (not strlist):
        return tuple(r_list)

    if strlist.value[0].lower() in ['a','e','i','o','u']:
        if r_list[0].value == None:
            r_list[0] = Node(strlist.value, None)
        else:
            r_list[0] = Node(r_list[0].value, Node(strlist.value, None))

    if (strlist.value[0].isalpha()) and (not strlist.value[0].lower() in ['a','e','i','o','u']):
        if r_list[1].value == None:
            r_list[1] = Node(strlist.value, None)
        else:
            r_list[1] = Node(r_list[1].value, Node(strlist.value, None))

    if not strlist.value[0].isalpha():
        if r_list[2].value == None:
            r_list[2] = Node(strlist.value, None)
        else:
            r_list[2] = Node(r_list[2].value, Node(strlist.value, None))

    return split_list(strlist.rest, tuple(r_list))

print(Node("xyz", Node("Abc", Node("49ers", None))))
