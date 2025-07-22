def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s
    values = []
    is_complete = True
    split_val = 0
    i = 0
    to_ret = ''

    #split string into words
    while i < len(s):
        if is_complete:
            split_val = numRows
        else:
            if numRows == 2:
                is_complete = not is_complete
                continue
            split_val = numRows - 2

        if split_val > len(s):
            split_val = len(s)

        val =  s[i:i+split_val]
        if is_complete:
            #append leading spaces to complete the column
            val = ' ' + val + ' '
            if len(val) < numRows:
                val += ' ' * (numRows - len(val))
        # if is not cpmplete i revere is
        values.append(val if is_complete else val[::-1])
        i += split_val
        is_complete = not is_complete
    #print(values)
    # stampo ricostruisco la stringa dalla matrice
    for j in range(numRows):
        for i in range(len(values)):
            if j >= len(values[i]):
                continue
            c = values[i][j]
            if c != ' ':
                to_ret += c
    return to_ret



if __name__ == "__main__":
    val = convert("paypalishiring",2)
    print(val)
    val = convert("ABCDE",4)
    print(val)
