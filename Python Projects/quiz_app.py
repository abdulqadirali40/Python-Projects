questions = ("What is the capital of France?",
             "Which planet is known as the Red Planet?",
             "What does HTML stand for?",
             "Who is known as the father of the computer?",
             "What is the value of Pi (π) approximately?")

options = (("A. Rome", "B. Paris", "C. Berlin", "D. Madrid"),
           ("A. Venus", "B. Saturn", "C. Mars", "D. Jupiter"),
           ("A. Hyper Text Markdown Language", "B. Hyperlink and Text Markup Language", "C. Hyper Text Markup Language", "D. Home Tool Markup Language"),
           ("A. Charles Babbage", "B. Alan Turing", "C. Steve Jobs", "D. Bill Gates"),
           ("A. 3.12", "B. 3.14", "3. 3.16", "4. C.18"))

answers = ("B", "C", "C", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")