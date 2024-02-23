while True:
    # Ask the user to guess the year Python 1.0 was released
    guess = int(input("When was Python 1.0 released? "))
    
    # Check the user's guess
    if guess == 1994:
        print("Correct!")
        break  # Exit the loop (and program) since the correct year was guessed
    elif guess < 1994:
        print("It was later than that!")
    else:  # This covers the case where guess > 1994
        print("It was earlier than that!")