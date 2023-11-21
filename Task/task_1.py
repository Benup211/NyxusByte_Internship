"""1.	Write a program that takes a number as input from the user and prints all the even numbers up to that number using a loop and conditional statement."""
try:
    user_input_value=int(input("Enter any positive number:"))
    print(f"All even number upto {user_input_value} is:")
    for i in range(user_input_value):
        if i%2==0:
            print(i,end=" ")
    print("\n")
except:
    print("User input should be number only")