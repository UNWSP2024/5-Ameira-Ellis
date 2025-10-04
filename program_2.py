# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as
import random

def math_quiz():
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)

    print(f"What is the sum of: ")
    print("  ", num1)
    print("+ ", num2)
    print("-----")

    correct_answer = num1 + num2
    user_answer = int(input("Your answer: "))
    if user_answer == correct_answer:
        print("Congratulations! Your answer is correct.")
    else:
        print(f"Sorry, the correct answer is {correct_answer}.")

num1 = random.randint(1, 500)
num2 = random.randint(1, 500)

print(f"What is the sum of: ")
print("  ", num1)
print("+ ", num2)
print("-----")

correct_answer = num1 + num2
user_answer = int(input("Your answer: "))
if user_answer == correct_answer:
    print("Congratulations! Your answer is correct.")
else:
    print(f"Sorry, the correct answer is {correct_answer}.")
math_quiz()







# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.