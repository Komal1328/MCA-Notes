def count_chars(sentence):
    num_digits = 0
    num_uppercase = 0
    num_lowercase = 0
    
    for char in sentence:
        if char.isdigit():
            num_digits += 1
        elif char.isupper():
            num_uppercase += 1
        elif char.islower():
            num_lowercase += 1
    
    return num_digits, num_uppercase, num_lowercase

sentence = "Hello World! 123"
num_digits, num_uppercase, num_lowercase = count_chars(sentence)
print("Number of digits:", num_digits)
print("Number of uppercase letters:", num_uppercase)
print("Number of lowercase letters:", num_lowercase)
