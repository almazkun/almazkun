def print_dir(i):
    """Somtimes usful to print the dir() of the object

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
