# Python implementation to compute # number of characters, words, spaces
# and lines in a file

# Function to count number
# of characters, words, spaces
# and lines in a file
fname = 'Sample.txt'
def counter(fname):
    # variable to store total word count
    num_words = 0
    num_words1 = 0
    
    # variable to store total line count
    num_lines = 0
    num_lines1 = 0
	
    # variable to store total character count
    num_charc = 0
	
    # variable to store total space count
    num_spaces = 0
	
    # opening file using with() method so that file gets closed
    # after completion of work
    with open(fname, 'r') as f:
        		
        # loop to iterate file line by line
        list_line = f.readlines()
        for line in list_line:
            num_lines1 += 1
            word = line.split()
	    print (word)
	    for i in word:
                print("i in word: ",i)
        for line in f:
            		
            # incrementing value of num_lines with each
	    # iteration of loop to
            # store total line count
            print("line: ",line)
            num_lines += 1
            
            # declaring a variable word and assigning its value as Y
	    # because every file is supposed to start with
	    # a word or a character
            word = 'Y'
	    # loop to iterate every
            # line letter by letter
            for letter in line:
                print("Letter: ",letter)
			
                # condition to check # that the encountered character
                # is not white space and a word
                if (letter != ' ' and word == 'Y'):
				
                    # incrementing the word count by 1
                    num_words += 1

                    # assigning value N to
                    # variable word because until
                    # space will not encounter
                    # a word can not be completed
                    word = 'N'

                    # condition to check that the encountered character
                    # is a white space
                elif (letter == ' '):
					
                    # incrementing the space count by 1
                    num_spaces += 1
		    	
                    # assigning value Y to
                    # variable word because after
                    # white space a word
                    # is supposed to occur
                    word = 'Y'
			
		# loop to iterate every letter
		# character by character
                #for i in letter:
                    #print("i in letter: ",i)
				
                    # condition to check
                    # that the encountered character
                    # is not white space and not
                    # a newline character
                if(letter != " " and letter != "\n"):
                                    		
                    # incrementing character count by 1
                    num_charc += 1
						
    # printing total word count
    print("Number of words in text file: ", num_words)
	
    # printing total line count
    print("Number of lines in text file: ", num_lines)
	
    # printing total character count
    print('Number of characters in text file: ', num_charc)
    # printing total space count
    print('Number of spaces in text file: ', num_spaces)
	
# Driver Code:
if __name__ == '__main__':
	fname = 'Sample.txt'
	try:
		counter(fname)
	except:
		print('File not found')
