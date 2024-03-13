
#Read a text file and display first five lines and last five lines in python

infile = "fileIntro.txt"

# Enter N value

# Opening the given file in read-only mode
with open(infile, 'r') as filedata:

    # Read the file lines using readlines()
    linesList= filedata.readlines()
    print("The following are the first 5 lines of a text file:")

    # Traverse in the list of lines to retrieve the first 5 lines of a file
    for textline in (linesList[:5]):

        # Printing the first 5 lines of the file line by line.
        #print(textline, end ='')
        print(textline)

    # Traverse in the list of lines to retrieve the last 5 lines of a file
    print("Lines from the last")
    for textline in (linesList[-5:]):

        # Printing the last 5 lines of the file line by line.
        #print(textline, end ='')
        print(textline)

# Closing the input file
filedata.close()

