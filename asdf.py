# Quiz Game

print("Welcome to the Quiz Game!")

# Questions and Answers
questions = ["What is the capital of France?", "Who invented the telephone?", "What year did World War II end?"]
answers = ["Paris", "Alexander Graham Bell", "1945"]

# Loop through questions and ask user for answers
score = 0
for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Your answer: ")
    if user_answer.lower() == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

# Print final score
print("Quiz complete! Your score is: ", score, " out of ", len(questions))

