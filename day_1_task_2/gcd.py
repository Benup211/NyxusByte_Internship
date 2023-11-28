"""Write a program that takes two numbers as input and finds out the GCD(greatest common divisor) of the two numbers using the Euclidean algorithm."""
while(True):
    to_continue='y'
    try:
        user_input_numbers=[]
        for i in range(2):
            user_input_numbers.append(abs(int(input(f"Enter {i+1} positive number:"))))
        a=max(user_input_numbers)
        b=min(user_input_numbers)
        def GCD(x,y):
            temp=x%y
            if (temp==0):
                return y
            else:
                return GCD(y,temp)
        print(f"GCD of {user_input_numbers[0]} and {user_input_numbers[1]} is {GCD(a,b)}")
        break
    except:
        print("Enter integer only")
        if to_continue!=input("Do you want to continue[y/n]"):
            break
