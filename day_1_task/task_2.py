"""2.	Create a guessing game where the user has to guess a number between 1 and 100. Use a loop to give the user 3 attempts, and provide hints (higher/lower) based on their guesses until they get it right.
"""
import random
try:
    guessed=False
    random_gen_number=random.randint(1,100)
    while(True):
        to_continue=False
        for i in range(3):
            user_input_number=int(input("Guess any number betn 1-100:"))
            if user_input_number==random_gen_number:
                guessed=True
                break
            elif user_input_number<=random_gen_number:
                print(f"Try guessing higher number than {user_input_number}")
            elif user_input_number<0:
                print("Enter positive value")
            else:
                print(f"Try guessing lower number than {user_input_number}")
        if(guessed):
            print("Sucessfully guessed number:",random_gen_number)
        else:
            continue_guess=input("Do you want to continue[y/n]:").lower()
            if continue_guess=='y':
                to_continue=True
        if not to_continue:
            print("Too bad! Number is",random_gen_number)
            break
except:
    print("User input should be number only")