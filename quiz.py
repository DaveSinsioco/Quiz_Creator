# initializes files for appendices
questions = []
first_choices = []
second_choices = []
third_choices = []
fourth_choices = []
answers = []

# initializes question count
question_count = 0

while True:

    # increment question count for each question
    question_count += 1

    # ask the user for question, choices, answer
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

    answer = input("Enter the answer (A/B/C/D): ") 
    answers.append(answer)

    # ask if the user wants to add another question
    add_another = input("Do you want to add another question? (y/n): ")
    if add_another.lower() != 'y':
        break

# replicates the saved question and answer to new appendices for user to try and now affect the main appendix

quiz_questions = questions
quiz_first_choices = first_choices
quiz_second_choices = second_choices
quiz_third_choices = third_choices
quiz_fourth_choices = fourth_choices
quiz_answers = answers

# adds a code tester for the quiz maker

# randomizes the questions
import random

# asks the user if they want to answer the questions
answer_questions = input("Do you want to answer the questions? (y/n): ")
if answer_questions.lower() != 'y':
    print("Exiting the quiz.")
    exit()

while True:
    i= random.randint(0, len(quiz_questions)- 1)
    print(f"Question: {quiz_questions[i]}")
    print(f"A: {quiz_first_choices[i]}")
    print(f"B: {quiz_second_choices[i]}")
    print(f"C: {quiz_third_choices[i]}")
    print(f"D: {quiz_fourth_choices[i]}")

    user_answer = input("Enter your answer (A/B/C/D): ")
    if user_answer.upper() == quiz_answers[i]:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {quiz_answers[i]}.")

    # removes the question from the list
    quiz_questions.pop(i)
    quiz_first_choices.pop(i)
    quiz_second_choices.pop(i)
    quiz_third_choices.pop(i)
    quiz_fourth_choices.pop(i)
    quiz_answers.pop(i)

# asks the user if they want to answer another question
    answer_again = input("Do you want to answer another question? (y/n): ")
    try:
        if answer_again.lower() != 'y':
            break
    except ValueError:
        print("Invalid input. Please enter 'y' or 'n'.")
