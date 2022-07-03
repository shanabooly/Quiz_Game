#quiz game
correct = 0

print("Welcome to my quiz. This will test your knowledge on European capital cities. \n")

answer = input("Do you want to play? \n")
if answer.lower() == "yes":
    print("\nGreat. Let's play!")
else:
    print("\nMaybe another time. Goodbye!")
    quit()
print("\n_______________________________________")


answer = input("\n\nWhat is the capital city of the France? \n")
if answer.lower() == "paris":
    correct += 1
    print("\nCorrect. " + str(correct) + "/1")
else:
    print("\Incorrect. " + str(correct) + "/1")
print(str(correct) +  "/1")
print("\n_______________________________________")


answer = input("\n\nWhat is the capital city of Germany? \n")
if answer.lower() == "berlin":
    print("\nCorrect")
    correct += 1
else:
    print("\nIncorrect!")
print(str(correct) + "/2")
print("\n_______________________________________")


answer = input("\n\nWhat is the capital city of Poland? \n")
if answer.lower() == "warsaw":
    print("\nCorrect")
    correct += 1
else:
    print("\nIncorrect!")
print(str(correct) + "/3")
print("\n_______________________________________")


answer = input("\n\nWhat is the capital city of Austria? \n")
if answer.lower() == "vienna":
    print("\nCorrect")
    correct += 1
else:
    print("\nIncorrect!")
print(str(correct) + "/4")
print("\n_______________________________________")


answer = input("\n\nWhat is the capital city of Norway? \n")
if answer.lower() == "oslo":
    print("\nCorrect")
    correct += 1
else:
    print("\nIncorrect!")
print(str(correct) + "/5")
print("\n_______________________________________")


calc = correct / 5 * 100
print("_______________________________________\n")

print("\nQuiz finished. You scored " + str(calc) + "%.")
