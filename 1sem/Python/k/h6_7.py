def my_sum(*numbers):
    result = 0
    for number in numbers:
        if type(number)==list:
            result += sum(number)
        else:
            result += number
    return result


def multiply(*numbers):
    result = 1
    for number in numbers:
        if type(number)==list:
            for i in number:
                result *= i
        else:
            result *= number
    return result

print(my_sum([1,2,3,4,5]))
print(multiply([1,2,3,4,5]))
