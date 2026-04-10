# Sylvia Schlotterbeck - CPT 135 Summer 2025 term
# Midterm Exam - July 7, 2025


"""
Instructions:

1. Collect User Grades (20 Points):

Create a loop that prompts the user to enter letter grades (A, A-, B, etc.).
The loop should continue until the user types a specific keyword (e.g., "done") to indicate they are finished.
As the user enters grades, store them in a list.

2. Create a Function to Convert Grades to GPA Points(40 Points)

Define a function that takes the list of grades as input and returns a list
of corresponding GPA points.

3. Create a function to display a table of individual GPA points and an
overall GPA (40 points)

Print out each grade with its corresponding GPA points and the overall GPA.
"""

grades_list = []
GPA_list = []
display_table = []

# this is the main function that calls the four helper functions of the program
def main():
    program_intro()
    collect_user_grades()
    convert_grades_to_GPA()
    display_results()
    
# this function introduces the user to the program, the program's function, and how it can be interacted with.    
def program_intro():
    print("*****************************")
    print("Welcome to E-Z-GPA Calculator")
    print("*****************************\n")
    print("About: this program stores as many grades as you wish to enter,")
    print("converts your letter grades into GPA scores, and calculates your final GPA.\n")
    print("(Note: this program uses the GPA scale as published in the \nCentral Maine Community College 2025-26 Academic Catalog)\n")
    input("Hit the 'Enter' or 'Return' key when you are ready to begin.\n")

# this function prompts user to input letter grades (A, A-, B+, etc.) until the user types "done"),
# and stores the user input as a list. Will function as intended whether the user types in upper or lower-case letters,
# but does not provide the fuctionality to handle input that lies outside the correct input options.
def collect_user_grades():
    grade = input('Please input your first grade (A, B, C+, etc.): ')
    grades_list.append(grade.lower())
    while True:
        grade = input("Please enter your next grade, or type 'Done' into the prompt and hit 'Enter' to display your GPA scores: ")
        if grade.lower() == 'done':
            break
        else:
            grades_list.append(grade.lower())
    return grades_list

# this function converts each element of grades_list into its corresponding GPA score, and appends
# that GPA score to the list called GPA_list
def convert_grades_to_GPA():
    for i in range(0,len(grades_list)):
        if grades_list[i] == 'a':
            GPA_list.append(4.00)
        elif grades_list[i] == 'a-':
            GPA_list.append(3.67)
        elif grades_list[i] == 'b+':
            GPA_list.append(3.33)
        elif grades_list[i] == 'b':
            GPA_list.append(3.00)
        elif grades_list[i] == 'b-':
            GPA_list.append(2.67)
        elif grades_list[i] == 'c+':
            GPA_list.append(2.33)
        elif grades_list[i] == 'c':
            GPA_list.append(2.00)
        elif grades_list[i] == 'c-':
            GPA_list.append(1.67)
        elif grades_list[i] == 'd+':
            GPA_list.append(1.33)
        elif grades_list[i] == 'd':
            GPA_list.append(1.00)
        elif grades_list[i] == 'f':
            GPA_list.append(0.00) 
    return GPA_list

# this function inputs data from grades_list and GPA_list into a new list and formats it to be displayed as a table,
# along with calculating the overall GPA score from the input grades and displaying that at the end.
def display_results():
    display_table = [('Grade' , 'GPA')]

    for i in range(0, len(GPA_list)):
        lower_case_grade = grades_list[i]
        display_table.append((f'{lower_case_grade.upper():^2}' , str(GPA_list[i])))
    display_table.append(('Overall GPA: ' , round(sum(GPA_list) / len(GPA_list),2)))
    
    for i in range(0,len(display_table)):
        print(*display_table[i])
        
if __name__ == "__main__":
    main()
