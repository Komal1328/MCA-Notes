strg = input("Enter the string: ")

def isPalindrome(strg):
    strg = strg.lower()
    for i in range(len(strg)):
        if(strg[i]!=strg[len(strg) - 1 - i]):
            return False
    return True

if(isPalindrome(strg)):
    print("Palindrome")
else:
    print("Not palindrome")