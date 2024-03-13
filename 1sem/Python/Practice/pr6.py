#pr6

str1=input("enter a string:").lower()

def palindrome(str1):
    for i in range(len(str1)):
        if(str1[i] != str1[len(str1)-1-i]):
            return False
    return True

if(palindrome(str1)):
    print("Palindrome")
else:
    print("Not Palindrome")
