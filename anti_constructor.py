def anti_constructor(function_object):
    if function_object.is_constructor:
        return True
    # return False
    vairables = function_object.variables_written
    judge = False
    for vairable in vairables:
        if vairable.is_constant:
            judge = True
        else:
            judge = False
    return judge