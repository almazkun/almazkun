def print_dir(i):
    """Somtimes usful to print the dir() of the object
    
    print_dir([])
    --------------------
    []
    __add__: ........... <method-wrapper '__add__' of list object at 0x7f7f6443be88>
    __class__: ......... <class 'list'>
    __contains__: ...... <method-wrapper '__contains__' of list object at 0x7f7f6443be88>
    __delattr__: ....... <method-wrapper '__delattr__' of list object at 0x7f7f6443be88>
    __delitem__: ....... <method-wrapper '__delitem__' of list object at 0x7f7f6443be88>
    __dir__: ........... <built-in method __dir__ of list object at 0x7f7f6443be88>
    __doc__: ........... list() -> new empty list
    list(iterable) -> new list initialized from iterable's items
    __eq__: ............ <method-wrapper '__eq__' of list object at 0x7f7f6443be88>
    __format__: ........ <built-in method __format__ of list object at 0x7f7f6443be88>
    __ge__: ............ <method-wrapper '__ge__' of list object at 0x7f7f6443be88>
    __getattribute__: .. <method-wrapper '__getattribute__' of list object at 0x7f7f6443be88>
    __getitem__: ....... <built-in method __getitem__ of list object at 0x7f7f6443be88>
    __gt__: ............ <method-wrapper '__gt__' of list object at 0x7f7f6443be88>
    __hash__: .......... None
    __iadd__: .......... <method-wrapper '__iadd__' of list object at 0x7f7f6443be88>
    __imul__: .......... <method-wrapper '__imul__' of list object at 0x7f7f6443be88>
    __init__: .......... <method-wrapper '__init__' of list object at 0x7f7f6443be88>
    __init_subclass__: . <built-in method __init_subclass__ of type object at 0x55c2e680c6a0>
    __iter__: .......... <method-wrapper '__iter__' of list object at 0x7f7f6443be88>
    __le__: ............ <method-wrapper '__le__' of list object at 0x7f7f6443be88>
    __len__: ........... <method-wrapper '__len__' of list object at 0x7f7f6443be88>
    __lt__: ............ <method-wrapper '__lt__' of list object at 0x7f7f6443be88>
    __mul__: ........... <method-wrapper '__mul__' of list object at 0x7f7f6443be88>
    __ne__: ............ <method-wrapper '__ne__' of list object at 0x7f7f6443be88>
    __new__: ........... <built-in method __new__ of type object at 0x55c2e680c6a0>
    __reduce__: ........ <built-in method __reduce__ of list object at 0x7f7f6443be88>
    __reduce_ex__: ..... <built-in method __reduce_ex__ of list object at 0x7f7f6443be88>
    __repr__: .......... <method-wrapper '__repr__' of list object at 0x7f7f6443be88>
    __reversed__: ...... <built-in method __reversed__ of list object at 0x7f7f6443be88>
    __rmul__: .......... <method-wrapper '__rmul__' of list object at 0x7f7f6443be88>
    __setattr__: ....... <method-wrapper '__setattr__' of list object at 0x7f7f6443be88>
    __setitem__: ....... <method-wrapper '__setitem__' of list object at 0x7f7f6443be88>
    __sizeof__: ........ <built-in method __sizeof__ of list object at 0x7f7f6443be88>
    __str__: ........... <method-wrapper '__str__' of list object at 0x7f7f6443be88>
    __subclasshook__: .. <built-in method __subclasshook__ of type object at 0x55c2e680c6a0>
    append: ............ <built-in method append of list object at 0x7f7f6443be88>
    clear: ............. <built-in method clear of list object at 0x7f7f6443be88>
    copy: .............. <built-in method copy of list object at 0x7f7f6443be88>
    count: ............. <built-in method count of list object at 0x7f7f6443be88>
    extend: ............ <built-in method extend of list object at 0x7f7f6443be88>
    index: ............. <built-in method index of list object at 0x7f7f6443be88>
    insert: ............ <built-in method insert of list object at 0x7f7f6443be88>
    pop: ............... <built-in method pop of list object at 0x7f7f6443be88>
    remove: ............ <built-in method remove of list object at 0x7f7f6443be88>
    reverse: ........... <built-in method reverse of list object at 0x7f7f6443be88>
    sort: .............. <built-in method sort of list object at 0x7f7f6443be88>
    ====================

    Args:
        i (object): Any dir()`able Python object
    """
    def get_longest(i):
        l = 1
        for x in dir(i):
            if len(x) > l:
                l = len(x)
        return l

    l = get_longest(i) + 1
    print('-' * ( l + 2 ))
    print(i)
    for x in dir(i):
        try:
            att = getattr(i, x)
        except Exception as e:
            att = e
        
        o = l - len(x)
        s = "." * o
        print(f"{x}: {s} {att}")
    print('=' * ( l + 2 ))
    
string = "Some sentence with words to be change to the branch name"
"".join([x.lower() for x in "-".join(string.split(" "))])
