# Intro to Python Homework Assignment: "Read and Display CSV Sales Data"
# Sylvia Schlotterbeck
# 6/22/25

"""
This program opens a .csv file, reads the file line by line into a list (with
each line of the file as one element in the list), and then prints out the
list to the terminal, with each line of the original file printed on its own
line in the terminal.
"""

line_list = [] # creates a list to store data from the file into

# defines the main function, which calls the read_sales_data function with
# 'sales.csv' as the input, and then prints the returned value of line_list
# line by line.
def main():
    read_sales_data('sales.csv')
    for line in line_list: # a for loop to print out the elements of line_list
                           # line by line
        print(line) 

# defines the read_sales_data function, which opens a file, then inputs lines
# of that file into the list line_list and returns the completed line_list to
# be used by the main function
def read_sales_data(filename):
    file = open(filename, 'r') # opens a file and assigns it as a file variable
                               # to the variable 'file'
    line = file.readline() # reads the header outside of the loop so it doesn't
                           # get inputted into the list
    for line in file: 
        line = line.rstrip('\n') # removes the '\n' from each line so output of
                                 # long_list will match the original content of
                                 # the file (i.e. no spaces between lines)
        line_list.append(line)   # appends each line of the file to the list 
    return line_list # returns the processed value of line_list so it can be
                     # used by the main function
    file.close()

if __name__ == "__main__":
    main()
