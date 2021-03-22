def __gcd(x, y):
    if x < y:
        x, y = y, x
    while y != 0:
        n = x%y
        x = y
        y = n
    return x

def gcd(input_list):
    output_list = list()
    for i in input_list:
        row = []
        for j in input_list:
            row.append(__gcd(i,j))
        output_list.append(row)

    return output_list
