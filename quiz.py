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
        # initialize the wrong answers and it's right answer to be shown at the end, counts wrong answers for scoring
        self.wrong_answers_question = []
        self.wrong_answers_first_choice = []
        self.wrong_answers_second_choice = []
        self.wrong_answers_third_choice = []
        self.wrong_answers_fourth_choice = []
        self.wrong_answers = []
        self.wrong_answer_count = 0

    # lets the user add questions, choices, and answers
    def add_questions(self):
        while True:
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
            self.answers.append(answer.upper())
            # checks if the answer is valid
            while answer.upper() not in ['A', 'B', 'C', 'D']:
                print("Invalid answer. Please enter A, B, C, or D.")
                answer = input("Enter the answer (A/B/C/D): ")
                self.answers[-1] = answer

            # ask if the user wants to add another question
            add_another_question = input("Do you want to add another question? (y/n): ")
            if add_another_question.lower() != 'y':
                break
        
    # asks the user if they want to answer the questions
    def ask_to_answer(self):
        answer_questions = input("Do you want to answer the questions? (y/n): ")
        if answer_questions.lower() != 'y':
            print("Exiting the quiz.")
            exit()

    # quiz taking function
    def take_quiz(self):

        while self.questions:
            num = random.randint(0, len(self.questions)- 1)
            print(f"Question: {self.questions[num]}")
            print(f"A: {self.first_choices[num]}")
            print(f"B: {self.second_choices[num]}")
            print(f"C: {self.third_choices[num]}")
            print(f"D: {self.fourth_choices[num]}")

            user_answer = input("Enter your answer (A/B/C/D): ")
            # checks if the answer is valid
            while user_answer.upper() not in ['A', 'B', 'C', 'D']:
                print("Invalid answer. Please enter A, B, C, or D.")
                user_answer = input("Enter your answer (A/B/C/D): ")

            # Check the answer
            self.check_answer(user_answer, num)

    # checks if the answer is correct
    def check_answer(self, user_answer, num):
        if user_answer.upper() != self.answers[num]:
            self.wrong_answer_count += 1
        
            # appends the wrong answers so it can be shown at the end, add count to wrong answers 
            self.wrong_answers_question.append(self.questions[num])
            self.wrong_answers_first_choice.append(self.first_choices[num])
            self.wrong_answers_second_choice.append(self.second_choices[num])
            self.wrong_answers_third_choice.append(self.third_choices[num])
            self.wrong_answers_fourth_choice.append(self.fourth_choices[num])
            self.wrong_answers.append(self.answers[num])
            
        # removes the question from the list
        self.questions.pop(num)
        self.first_choices.pop(num)
        self.second_choices.pop(num)
        self.third_choices.pop(num)
        self.fourth_choices.pop(num)
        self.answers.pop(num)

    # shows the score
    def show_score(self):
        quiz_score = (self.question_count - self.wrong_answer_count)
        print(f"Your score is {quiz_score} out of {self.question_count}.")
        
        # counts the wrong answer, if there are no wrong answers, it will not show the wrong answers
        if self.wrong_answer_count == 0:
            print("You got all the answers right!")
        else: 
            print("You got the following questions wrong:")
            for count in range(len(self.wrong_answers_question)):
                print(f"Question: {self.wrong_answers_question[count]}")
                print(f"A: {self.wrong_answers_first_choice[count]}")
                print(f"B: {self.wrong_answers_second_choice[count]}")
                print(f"C: {self.wrong_answers_third_choice[count]}")
                print(f"D: {self.wrong_answers_fourth_choice[count]}")
                print(f"Correct Answer: {self.wrong_answers[count]}")
                
        print("Thank you for taking the quiz!")


    # Main function to run the quiz
    def main(self):
        while True:
            self.add_questions()
            self.ask_to_answer()
            self.take_quiz()
            self.show_score()

            # ask if the user wants to take the quiz again
            take_quiz_again = input("Do you want to take the quiz again? (y/n): ")
            if take_quiz_again.lower() != 'y':
                print("Exiting the quiz.")
                break
            else:
                # reset the quiz
                self.__init__()

# Run the quiz
if __name__ == "__main__":
    quiz = Quiz()
    quiz.main()