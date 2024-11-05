'''
    Lesson: Input and F strings
    Author:Jinming Chen
    Date Created: Nove 05, 2024
    Date Last Modified: Nove 05, 2024
'''

def q1():
  #Write Assignment code here
# Ask the user to enter a word, and output that word back to the user
word = input("Input a word: ")
print(word)

def q2():
  #Write Assignment code here
# Ask the user to enter their name, and output "Hello" followed by their name, using concatenation
name = input("Enter your name: ")
print("Hello " + name)
def q3():
  #Write Assignment code here
# Ask the user to enter their first name, then have them enter their last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(last_name, first_name)

def q4():
  #Write Assignment code here

#Do not edit code below this comment
# Ask the user to enter the first student, then another student, output both students' names
student1 = input("Enter student: ")
student2 = input("Enter another student: ")
print(f"Your students are {student1} and {student2}")
q1()
q2()
q3()
q4()
