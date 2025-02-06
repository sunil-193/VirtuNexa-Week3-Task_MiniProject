import random

# Define the Flashcard class to store question and answer
class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

# Define the FlashcardApp class to manage flashcards, quizzes, and score tracking
class FlashcardApp:
    def __init__(self):
        self.flashcards = []
        self.score = 0
        self.total_questions = 0

    # Add a flashcard to the app
    def add_flashcard(self, question, answer):
        flashcard = Flashcard(question, answer)
        self.flashcards.append(flashcard)
        print("Flashcard added!")

    # Take a quiz with the flashcards
    def take_quiz(self):
        if not self.flashcards:
            print("No flashcards available. Please add some flashcards first.")
            return

        random.shuffle(self.flashcards)
        self.score = 0
        self.total_questions = len(self.flashcards)

        for flashcard in self.flashcards:
            print(f"Question: {flashcard.question}")
            user_answer = input("Your Answer: ")
            if user_answer.lower() == flashcard.answer.lower():
                print("Correct!")
                self.score += 1
            else:
                print(f"Incorrect! The correct answer is: {flashcard.answer}")
            print()

        self.show_score()

    # Show the user's score after the quiz
    def show_score(self):
        print(f"Your score: {self.score}/{self.total_questions}")

# Main function to run the app and handle user interactions
def main():
    app = FlashcardApp()

    while True:
        print("\nFlashcard App")
        print("1. Add Flashcard")
        print("2. Take Quiz")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            question = input("Enter the question: ")
            answer = input("Enter the answer: ")
            app.add_flashcard(question, answer)
        elif choice == '2':
            app.take_quiz()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
