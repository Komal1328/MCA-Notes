#h.6

def palindrom(str1):
    flag=0
    for i in range(len(str1)):
        if(str1[i] !=str1[len(str1)-1-i]):
            flag = 1
        return flag
str1=input("Enter a String: ")
res=palindrom(str1)
if(res==1):
    print("String is not palindrome")
else:
    print("String is palindrome")   
