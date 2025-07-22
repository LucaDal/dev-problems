def longestPalindrome(s: str):
    max = 0
    pal = ''
    slen =len(s)
    if slen == 1:
        return s
    for c in range(slen):
        startLeftCount = False
        l = c
        r = c + 1 if c+1 < slen else slen - 1
        cont = 0
        tempL, tempR = 0, 0
        while True:
            if(s[l] != s[r] and startLeftCount == True):
                break
            if l == 0 and r == slen - 1:
               break
            if(s[l] == s[r]):
                cont = r-l
                tempL, tempR = l, r

            if startLeftCount and r < slen -1:
                r += 1
            if l > 0:
                l -= 1
            startLeftCount = True
        if(max < cont):
            max = cont
            pal = s[tempL:tempR+1]
    return pal


#nn TODO: TEST
if __name__=="__main__":
    max = longestPalindrome("babad")
    print(max)
    max = longestPalindrome('a')
    print(max)
    max = longestPalindrome('cbbd')
    print(max)
    max = longestPalindrome('bb')
    print(max)
    max = longestPalindrome('aaca')
    print(max)



