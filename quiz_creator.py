# initializes the questions, choices, and answers in appendices
questions = []
first_choices = []
second_choices = []
third_choices = []
fourth_choices = []
answers = []

# initializes the count for each question
question_count = 0

while True:

    # increment the question count
    question_count += 1

    # asks the user to enter question, choices, answer
    question = input("Enter the question: ")
    choice1 = input("Enter the choice A: ")
    choice2 = input("Enter the choice B: ")
    choice3 = input("Enter the choice C: ")
    choice4 = input("Enter the choice D: ")
    answer = input("Enter the correct choice (A/B/C/D): ")