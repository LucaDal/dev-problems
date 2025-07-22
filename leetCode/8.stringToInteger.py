def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    val = 0
    start_val = False
    sign = 1
    start_eval = False
    max_int = 2**31 - 1
    for c in s:
        ascii_code = ord(c)
        if ascii_code == 46: # .
                break
        if not start_val and ascii_code == 45: # -
            sign = -1
            max_int += 1
        if (ascii_code >= 48 and ascii_code <= 57) or (ascii_code == 45 or ascii_code == 43): # 0 - 9
            if start_eval and (ascii_code == 45 or ascii_code == 43):
                break
            start_eval = True
            if (ascii_code == 45 or ascii_code == 43):
                continue
            if ascii_code != 48:
                start_val = True
            if start_val:
                val *= 10
                val += ascii_code - 48
        elif start_eval or (ascii_code >= 65 and ascii_code <= 122):
            break
        if val > max_int:
            return max_int * sign
    return val * sign

if __name__ == "__main__":
    print(myAtoi("42"))
    print(myAtoi("   -042"))
    print(myAtoi("000-1"))
    print(myAtoi("0-1"))
    print(myAtoi("0001-1"))
    print(myAtoi("afs iadn 987"))
    print(myAtoi("+-12"))
    print(myAtoi("-+12"))
