# Create an empty dictionary
student_dict = {}

# Ask the user to input 10 student names and their marks
for i in range(10):
    name = input("Enter name of student: ")
    marks = int(input("Enter marks of student: "))
    student_dict[name] = marks

# Sort the dictionary by marks in ascending order
sorted_dict = dict(sorted(student_dict.items(), key=lambda x: x[1]))

# Print the sorted dictionary
print("Sorted dictionary by marks:")
print(sorted_dict)
