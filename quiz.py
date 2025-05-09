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

# initialize the wrong answers and it's right answer to be shown at the end
wrong_answers_question = []
wrong_answers_first_choice = []
wrong_answers_second_choice = []
wrong_answers_third_choice = []
wrong_answers_fourth_choice = []
wrong_answers = []

# counts wrong answers for scoring
wrong_answer_count = 0

while True:
    i= random.randint(0, len(quiz_questions)- 1)
    print(f"Question: {quiz_questions[i]}")
    print(f"A: {quiz_first_choices[i]}")
    print(f"B: {quiz_second_choices[i]}")
    print(f"C: {quiz_third_choices[i]}")
    print(f"D: {quiz_fourth_choices[i]}")

    user_answer = input("Enter your answer (A/B/C/D): ")
    if user_answer.upper() != quiz_answers[i]:

        # appends the wrong answers so it can be shown at the end, add count to wrong answers 
        wrong_answers_question.append(quiz_questions[i])
        wrong_answers_first_choice.append(quiz_first_choices[i])
        wrong_answers_second_choice.append(quiz_second_choices[i])
        wrong_answers_third_choice.append(quiz_third_choices[i])
        wrong_answers_fourth_choice.append(quiz_fourth_choices[i])
        wrong_answers.append(quiz_answers[i])
        wrong_answer_count += 1

    # removes the question from the list

    quiz_questions.pop(i)
    quiz_first_choices.pop(i)
    quiz_second_choices.pop(i)
    quiz_third_choices.pop(i)
    quiz_fourth_choices.pop(i)
    quiz_answers.pop(i)

# shows the score
print(f"You got {(question_count) - wrong_answer_count} out of {(question_count)}.")

# shows the wrong answers at the end
print("You got the following questions wrong:")
for i in range(len(wrong_answers_question)):
    print(f"Question: {wrong_answers_question[i]}")
    print(f"A: {wrong_answers_first_choice[i]}")
    print(f"B: {wrong_answers_second_choice[i]}")
    print(f"C: {wrong_answers_third_choice[i]}")
    print(f"D: {wrong_answers_fourth_choice[i]}")
    print(f"Correct answer: {wrong_answers[i]}")

# thank user for using the quiz
print("Thank you for using the quiz!")