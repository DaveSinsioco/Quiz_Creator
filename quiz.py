import random

# Encalsulates all the functions in "Quiz"
class Quiz:
    def __init__(self):       
    # initializes files for appendices, initializes question count
        self.questions = []
        self.first_choices = []
        self.second_choices = []
        self.third_choices = []
        self.fourth_choices = []
        self.answers = []
        self.question_count = 0

    # let's the user add questions, choices, and answers
    def add_questions(self):

        # increment question count for each question, ask the user for question
        self.question_count += 1
        question = input(f"Enter question {self.question_count}: ")
        self.questions.append(question)

        # ask the user for choices, answer
        first_choice = input("Enter the choice A: ")
        self.first_choices.append(first_choice)

        second_choice = input("Enter the choice B: ")
        self.second_choices.append(second_choice)

        third_choice = input("Enter the choice C: ")
        self.third_choices.append(third_choice)

        fourth_choice = input("Enter the choice D: ")
        self.fourth_choices.append(fourth_choice)

        answer = input("Enter the answer (A/B/C/D): ") 
        self.answers.append(answer)

        # ask if the user wants to add another question
        add_another_question = input("Do you want to add another question? (y/n): ")
        if add_another_question.lower() != 'y':
            return
        
    # asks the user if they want to answer the questions
    def ask_to_answer(self):
        answer_questions = input("Do you want to answer the questions? (y/n): ")
        if answer_questions.lower() != 'y':
            print("Exiting the quiz.")
            exit()

    # quiz taking function
    def take_quiz(self):
        # initialize the wrong answers and it's right answer to be shown at the end, counts wrong answers for scoring
        self.wrong_answers_question = []
        self.wrong_answers_first_choice = []
        self.wrong_answers_second_choice = []
        self.wrong_answers_third_choice = []
        self.wrong_answers_fourth_choice = []
        self.wrong_answers = []
        self.wrong_answer_count = 0

quiz = Quiz()

while quiz_questions:
    num = random.randint(0, len(quiz_questions)- 1)
    print(f"Question: {quiz_questions[num]}")
    print(f"A: {quiz_first_choices[num]}")
    print(f"B: {quiz_second_choices[num]}")
    print(f"C: {quiz_third_choices[num]}")
    print(f"D: {quiz_fourth_choices[num]}")

    user_answer = input("Enter your answer (A/B/C/D): ")
    # checks if the answer is valid
    while user_answer.upper() not in ['A', 'B', 'C', 'D']:
        print("Invalid answer. Please enter A, B, C, or D.")
        user_answer = input("Enter your answer (A/B/C/D): ")

    # checks if the answer is correct
    if user_answer.upper() != quiz_answers[num]:
        
        # appends the wrong answers so it can be shown at the end, add count to wrong answers 
        wrong_answers_question.append(quiz_questions[num])
        wrong_answers_first_choice.append(quiz_first_choices[num])
        wrong_answers_second_choice.append(quiz_second_choices[num])
        wrong_answers_third_choice.append(quiz_third_choices[num])
        wrong_answers_fourth_choice.append(quiz_fourth_choices[num])
        wrong_answers.append(quiz_answers[num])
        wrong_answer_count += 1

    # removes the question from the list

    quiz_questions.pop(num)
    quiz_first_choices.pop(num)
    quiz_second_choices.pop(num)
    quiz_third_choices.pop(num)
    quiz_fourth_choices.pop(num)
    quiz_answers.pop(num)

# shows the score
print(f"Your score is {(quiz.question_count) - wrong_answer_count} out of {(quiz.question_count)}.")

# counts the wrong answer, if there are no wrong answers, it will not show the wrong answers
if wrong_answer_count == 0:
    print("You got all the answers right!")
else: 
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