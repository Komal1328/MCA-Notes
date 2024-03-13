#h6.13


def palindrome(str1):
    for i in range(len(str1)):
        if(str1[i] !=str1[len(str1)-1-i]):
            return False
        else:
            return True
st=input("Enter a sentence: ")
slst=list(st.split(" "))
count=0
for i in slst:
    res=palindrome(i)
    if(res==True):
        count=count+1
    else:
        count=count+0
print("Numbber of palindrome strings are :",count)

    
    
