def list_accumulator(nested_list):
    sum = 0
    for i in nested_list:
        if type(i) is list:
            sum += list_accumulator(i)
        else:
            sum += i

    return sum
