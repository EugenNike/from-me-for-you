def good_dreams(text, first_divisor, second_divisor, *args, **kwargs):
    lst = text.split(first_divisor)
    b_sp = []
    for mini_sp in lst:
        b_sp.append(mini_sp.split(second_divisor))
    edit_sp = [] * len(b_sp)
    for arg in args:
        for_edit = b_sp[arg[1]]
        if arg[0] in kwargs:
            func_edit = kwargs[arg[0]]
            edit_sp.insert(arg[1], list(map(func_edit, for_edit)))
        else:
            pass
    for i in edit_sp:
        print(i)



print(*good_dreams(
    'And, who is this Pinocchio? - They say he\'s a bad, lazy, dangerous type. - Slander, pure slander!',
    ' - ',
    ', ',
    ('not_before', 2),
    ('up_low', 0),
    ('title', 1),
    ('abracodabra', 1),
    up_low=lambda x: ''.join([x[i].lower() if i % 2 else
    x[i].upper() for i in range(len(x))]),
    not_before=lambda x: f'not {x}',
    title=lambda x: x.title()
    ), sep='\n')
