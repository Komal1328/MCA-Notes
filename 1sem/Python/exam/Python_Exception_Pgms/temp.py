filename = input("Enter the file name: ")
search_str = "#"
matching_lines = []
with open(filename, 'r') as f:
    contents = f.read()
    lines = contents.split('\n')
    for line in lines:
        if search_str in line:
            matching_lines.append(line.strip())

for line in matching_lines:
    print(line)

print()
print(contents)
