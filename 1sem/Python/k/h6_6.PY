def isPalindrome(strg):
    for i in range(len(strg)):
        if(strg[i]!=strg[len(strg)-1-i]):
            return False
    return True

print(isPalindrome("abba"))