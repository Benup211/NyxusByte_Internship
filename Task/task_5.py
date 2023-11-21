"""5.	Design a simple calculator that asks the user for two numbers and an operation (addition, subtraction, multiplication, division) and performs the calculation using conditional statements and user input.
"""
user_input_number=[]
for i in range(2):
    val=int(input(f"Enter {i+1} number:"))
    user_input_number.append(val)
def calculator(two_number):
    print("Calculation")
    operator=input("Enter + for addition\n- for subtraction\n/ for division\n* for multiplication\nEnter value:")
    if operator is '+':
        return two_number[0]+two_number[1]
    elif operator is '-':
        return two_number[0]-two_number[1]
    elif operator is '/':
        return two_number[0]/two_number[1]
    elif operator is '*':
        return two_number[0]*two_number[1]
    else:
        print("Error Invalid operator")
print(calculator(user_input_number))