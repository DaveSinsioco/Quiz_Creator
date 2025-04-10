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
    question = input(f"Enter the question #{question_count}: ")
    questions.append(question)

    first_choice = input("Enter the choice A: ")
    first_choices.append(first_choice)

    second_choice = input("Enter the choice B: ")
    second_choices.append(second_choice)

    third_choice = input("Enter the choice C: ")
    third_choices.append(third_choice)

    fourth_choice = input("Enter the choice D: ")
    fourth_choices.append(fourth_choice)

    answer = input("Enter the correct choice (A/B/C/D): ")
    answers.append(answer)

    # asks the user if they want to add another question
    add_another = input("Do you want to add another question? (y/n): ")
    try: 
        if add_another.lower() != 'y':
            break
    except ValueError:
        print("Invalid input. Please enter 'y' or 'n'.")

# testing the code        

# randomizes the questions
import random

while True:
    i = random.randint(0, len(questions) - 1)
    print("Question:", questions[i])
    print("A:", first_choices[i])
    print("B:", second_choices[i])
    print("C:", third_choices[i])
    print("D:", fourth_choices[i])

    user_answer = input("Enter your answer (A/B/C/D): ")
    if user_answer.upper() == answers[i]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", answers[i])

    answer_again = input("Do you want to answer another question? (y/n): ") 
    try:
        if answer_again.lower() != 'y':
            break   
    except ValueError:
        print("Invalid input. Please enter 'y' or 'n'.")