filename = input("Enter file name: ")
with open(filename, 'r') as f:
    content = f.read()
    char_count = len(content)
    word_count = len(content.split())
    line_count = len(content.splitlines())

print(char_count)
print(word_count)
print(line_count)