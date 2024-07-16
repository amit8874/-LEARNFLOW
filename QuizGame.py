import random

# Define quiz questions
questions = {
    "science": {
        "easy": [
            ("What planet is known as the Red Planet?", "Mars"),
            ("What is the chemical symbol for water?", "H2O")
        ],
        "medium": [
            ("What is the powerhouse of the cell?", "Mitochondria"),
            ("What element does 'O' represent on the periodic table?", "Oxygen")
        ],
        "hard": [
            ("What is the second most abundant element in the Earth's crust?", "Silicon"),
            ("What is the atomic number of carbon?", "6")
        ]
    },
    "history": {
        "easy": [
            ("Who was the first president of the United States?", "George Washington"),
            ("In which year did the Titanic sink?", "1912")
        ],
        "medium": [
            ("Who wrote the Declaration of Independence?", "Thomas Jefferson"),
            ("What year did World War I begin?", "1914")
        ],
        "hard": [
            ("Who was the British Prime Minister during World War II?", "Winston Churchill"),
            ("In which year was the Berlin Wall torn down?", "1989")
        ]
    }
}

# Function to ask questions
def ask_question(question, answer):
    user_answer = input(f"{question} ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        return True
    else:
        print(f"Incorrect! The correct answer was {answer}.")
        return False

# Main quiz game function
def quiz_game():
    print("Welcome to the Quiz Game!")
    topic = input("Choose a topic (science/history): ").lower()
    while topic not in questions:
        print("Invalid topic. Please choose again.")
        topic = input("Choose a topic (science/history): ").lower()
    
    difficulty = input("Choose a difficulty level (easy/medium/hard): ").lower()
    while difficulty not in questions[topic]:
        print("Invalid difficulty level. Please choose again.")
        difficulty = input("Choose a difficulty level (easy/medium/hard): ").lower()
    
    score = 0
    question_set = questions[topic][difficulty]
    random.shuffle(question_set)
    
    for question, answer in question_set:
        if ask_question(question, answer):
            score += 1
    
    print(f"Your final score is: {score}/{len(question_set)}")

# Start the game
if __name__ == "__main__":
    quiz_game()
