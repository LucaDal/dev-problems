def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    sign = -1 if x < 0 else 1
    val = int(str(abs(x))[::-1]) * sign
    max = pow(2,31)
    if val > max-1 or val < -max:
        return 0
    return val

if __name__ == "__main__":
    val = reverse(123)
    print(val)
    val = reverse(1230000)
    print(val)
    val = reverse(1230000)
    print(val)
