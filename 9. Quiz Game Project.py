# -------------------------
# QUIZ GAME
# -------------------------
# Flow of the program:
# 1. Start
# 2. Load high score from the file
# 3. Ask player name
# 4. Show questions one by one
# 5. Take answers
# 6. Check answers
# 7. Increase score if correct
# 8. After quiz ends, compare with high score
# 9. Save high score if beaten
# 10. End
# -------------------------

# File to store high score
file_name = "high_score.txt"

# Global variables
score = 0        # Current game score
high_score = 0   # Highest score ever

# -------------------------
# Load High Score
# Reads previous high score from the file
# If file doesn't exist, high_score stays 0
# -------------------------
def load_high_score():
    global high_score
    try:
        file = open(file_name, "r")      # Open file in read mode
        high_score = int(file.read())    # Read high score and convert to integer
        file.close()                     # Close the file
    except:
        # If file not found or empty, high_score remains 0
        pass

# -------------------------
# Save High Score
# Saves new high score to the file
# -------------------------
def save_high_score():
    file = open(file_name, "w")          # Open file in write mode
    file.write(str(high_score))          # Write high score as string
    file.close()                         # Close file

# -------------------------
# Play Quiz
# Asks all questions, checks answers, updates score
# -------------------------
def play_quiz():
    global score

    # List of questions
    questions = [
        "What is output of print(2+3)?",
        "Which data type stores true/false",
        "Which keyword is used to fetch global variable in the function?"
    ]

    # List of correct answers (same order as questions)
    answers = ["5", "bool", "global"]

    # Loop through all questions
    for i in range(len(questions)):
        print("\nQ.", questions[i])        # Show question
        user_answer = input("Your answer: ")  # Take input from player
        if user_answer == answers[i]:      # Check if answer is correct
            score = score + 1              # Increase score
            print("Correct")
        else:
            print("Wrong")                 # Answer is incorrect

# -------------------------
# Main Program
# Controls the quiz game flow
# -------------------------
def main():
    global high_score

    load_high_score()                       # Load previous high score

    name = input("Enter your name: ")       # Ask player name

    play_quiz()                             # Start the quiz

    # Show final score
    print("\nQuiz over")
    print(name, "Your score is:", score)

    # Compare with high score
    if score > high_score:
        high_score = score                  # Update high score
        save_high_score()                   # Save new high score
        print("Congratulations! You set a new high score!")
    else:
        print("High score is:", high_score)  # Show previous high score

# Run the quiz
main()