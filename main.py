#quiz game
correct = 0
guesses = 0

print(
    "Welcome to my quiz. This will test your knowledge on European capital cities. \n"
)

answer = input("Do you want to play? \n\n")
if answer.lower() == "yes":
    print("\nGreat. Let's play!")
else:
    print("\nMaybe another time. Goodbye!")
    quit()
print("\n_______________________________________")

answer = input("\n\nWhat is the capital city of the France? \n")
if answer.lower() == "paris":
    correct += 1
    guesses += 1
    print("\nCorrect. " + str(correct) + "/" + str(guesses))
else:
    guesses += 1
    print("\nIncorrect. " + str(correct) + "/" + str(guesses))
print("\n_______________________________________")

answer = input("\n\nWhat is the capital city of Germany? \n")
if answer.lower() == "berlin":
    guesses += 1
    correct += 1
    print("\nCorrect. " + str(correct) + "/" + str(guesses))
else:
    guesses += 1
    print("\nIncorrect. " + str(correct) + "/" + str(guesses))
print("\n_______________________________________")

answer = input("\n\nWhat is the capital city of Poland? \n")
if answer.lower() == "warsaw":
    guesses += 1
    correct += 1
    print("\nCorrect. " + str(correct) + "/" + str(guesses))
else:
    guesses += 1
    print("\nIncorrect. " + str(correct) + "/" + str(guesses))

print("\n_______________________________________")

answer = input("\n\nWhat is the capital city of Austria? \n")
if answer.lower() == "vienna":
    guesses += 1
    correct += 1
    print("\nCorrect. " + str(correct) + "/" + str(guesses))
else:
    guesses += 1
    print("\nIncorrect. " + str(correct) + "/" + str(guesses))
print("\n_______________________________________")

answer = input("\n\nWhat is the capital city of Norway? \n")
if answer.lower() == "oslo":
    guesses += 1
    correct += 1
    print("\nCorrect. " + str(correct) + "/" + str(guesses))
else:
    guesses += 1
    print("\nIncorrect. " + str(correct) + "/" + str(guesses))
print("\n_______________________________________")

calc = correct / 5 * 100
print("_______________________________________\n")

print("\nQuiz finished. You scored " + str(calc) + "%.")
