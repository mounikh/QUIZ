import time
import random

class Quiz:
    def __init__(self):
        self.questions = [
            {
                'question': 'What is the capital of Python?',
                'options': ['A. Monty', 'B. Pythopolis', 'C. Pydonia', 'D. None of the above'],
                'answer': 'D'
            },
            {
                'question': 'Which of the following is not a data type in Python?',
                'options': ['A. int', 'B. float', 'C. complex', 'D. long'],
                'answer': 'D'
            },
            {
                'question': 'Which of the following statements is used to exit from a loop in Python?',
                'options': ['A. stop', 'B. exit', 'C. break', 'D. end'],
                'answer': 'C'
            },
            {
                'question': 'Which of the following is a valid way to create a list in Python?',
                'options': ['A. list = [1, 2, 3, 4]', 'B. list(1, 2, 3, 4)', 'C. list = {1, 2, 3, 4}', 'D. list(1, 2, 3, 4)'],
                'answer': 'A'
            },
            {
                'question': 'How do you declare a variable in Python?',
                'options': ['A. var x = 5', 'B. x = 5', 'C. int x = 5', 'D. $x = 5'],
                'answer': 'B'
            },
        ]
        self.score = 0
        self.student_name = ''
        self.roll_number = ''
        self.user_answer = None  # To store user's answer

    def display_login_page(self):
        print("Welcome to the Python Quiz App!")

        # Validate and get the student name
        while True:
            self.student_name = input("Enter your name: ")
            if self.validate_name():
                break
            else:
                print("Invalid name. Please enter only alphabets.")

        # Validate and get the roll number
        while True:
            self.roll_number = input("Enter your roll number: ")
            if self.validate_roll_number():
                break
            else:
                print("Invalid roll number. Please enter 11 digits.")

    def validate_name(self):
        return self.student_name.isalpha()

    def validate_roll_number(self):
        return self.roll_number.isdigit() and len(self.roll_number) == 11

    def validate_login(self):
        return self.validate_name() and self.validate_roll_number()

    def countdown_timer(self, seconds):
        start_time = time.time()
        while time.time() - start_time < seconds:
            time.sleep(1)
        print("\nTime's up!\n")

    def take_quiz(self):
        for i, question in enumerate(self.questions):
            self.user_answer = None  # Reset user's answer for each question
            self.display_question(question)

            # Get user's answer within the specified time
            self.get_user_answer()

            # Start countdown timer for 10 seconds after the user has answered
            if self.user_answer is not None:
                print("\nChecking your answer...\n")
                self.countdown_timer(10)

                if self.user_answer.upper() == question['answer']:
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Wrong! The correct answer is {question['answer']}\n")
            else:
                print("\nMoving to the next question...\n")

    def get_user_answer(self):
        start_time = time.time()
        while time.time() - start_time < 10:
            self.user_answer = input("Your answer: ")
            if self.user_answer:
                break

    def display_question(self, question):
        print(question['question'])
        for option in question['options']:
            print(option)

    def display_correct_answers(self):
        print("Correct Answers:")
        for i, question in enumerate(self.questions, start=1):
            print(f"{i}. {question['answer']}")

    def display_score(self):
        print(f"Quiz ended. Your score is: {self.score}/{len(self.questions)}")
        self.display_correct_answers()

    def save_results(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open("quiz_results.txt", "a") as file:
            file.write(f"{timestamp} - {self.student_name}, {self.roll_number}: {self.score}/{len(self.questions)}\n")

    def run(self):
        self.display_login_page()
        if self.validate_login():
            random.shuffle(self.questions)  # Shuffle question order
            self.take_quiz()
            self.display_score()
            self.save_results()

if __name__ == "__main__":
    quiz = Quiz()
    quiz.run()
