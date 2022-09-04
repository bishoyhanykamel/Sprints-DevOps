def myFunc(number_list, float_list):
    mean_value = []
    total_value = 0
    max_float = -1.0

    for x in number_list:
        if type(x) == type(1):
            if x % 2 == 0:
                mean_value.append(x)
                total_value = total_value + x


    for x in float_list:
        if type(x) == type(0.0):
            if x > max_float:
                max_float = x
    
    if max_float == -1.0 or len(mean_value) == 0:
        return 0
    
    return (total_value//len(mean_value), max_float)





