secretnum = 58
attempts = 7
won = False

print ("Guess a number between 1 and 100")
print ("You have 7 chances \n")

for i in range(attempts):
    guess = int(input(f"Attempt {i+1}: Enter your guess: "))

    if guess == secretnum:
        print("You guessed the number!")
        won = True
    
    elif guess < secretnum: 
        print ("It's higher")

    else: 
        print ("It's lower")

    if i == attempts - 2 and not won:
        if secretnum % 2 == 0:
            print ("Here is a hint: The secret number ends with an even digit.")
        else: 
            print ("Here is a hint: The secret number ends with an odd digit.")

if won: 
    print ("You are a genius, you won!")
else:
    print ("You ran out of attempts.")
    print ("The secret number was", secretnum)



