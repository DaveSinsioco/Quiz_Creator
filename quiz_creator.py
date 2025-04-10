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
    questions.append(question)

    first_choice = input("Enter the choice A: ")
    first_choices.append(choice1)

    second_choice = input("Enter the choice B: ")
    second_choices.append(choice2)

    third_choice = input("Enter the choice C: ")
    third_choices.append(choice3)

    fourth_choice = input("Enter the choice D: ")
    fourth_choices.append(choice4)

    answer = input("Enter the correct choice (A/B/C/D): ")
    answers.append(answer)