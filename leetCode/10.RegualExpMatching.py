def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    dot = '.'
    star = '*'
    temp_c = ''
    idx_p = 0
    len_p = len(p)
    for i in range(len(s)):
        if idx_p >= len_p:
            return False
        if p[idx_p] == dot:
            temp_c = dot
            idx_p += 1
            continue
        elif p[idx_p] == star and (temp_c == s[i] or temp_c == dot):
            idx_p += 1
            continue
        elif p[idx_p] != s[i]:
            if (idx_p + 2 < len_p) and p[idx_p + 1] == star:
                if p[idx_p + 2] == s[i]:
                    idx_p += 3
                    temp_c = s[i]
                    continue
            return False
        else:
            idx_p += 1
        temp_c = s[i]
    return True


if __name__ == "__main__":
  #  isMatch("aa","a")
  #  isMatch("aa","a*")
  #  isMatch("aa",".*")
#   print( isMatch("aa","c*a*b"))
   print( isMatch("aab","c*a*b"))
