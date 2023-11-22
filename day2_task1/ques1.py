"""Write a programthatpromptstheusertoenteranumber.Createalistofsquaresofallnumbersfrom1totheuser-enterednumber."""
try:
    user_input_number=int(input("Enter a number:"))
    square_list=list()
    for i in range(1,user_input_number+1):
        square_list.append(i*i)
    print(f"Square from 1 number to {user_input_number} is {square_list} ")
except ValueError as e:
    print(f"Error occur {e}")