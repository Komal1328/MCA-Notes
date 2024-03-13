def isPalindrome(str):
     for i in range(len(str)):
          if(str[i]!=str[len(str) - 1 - i]):
               return False
     return True
strg = input("Enter the sentence: ")
lst = strg.split(" ")
for i in lst:
     if(isPalindrome(i)):
          print(i)

