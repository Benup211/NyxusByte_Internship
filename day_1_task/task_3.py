"""3.	Write a program that takes N numbers as input from a user and puts them in a list. Then the program should find out the sum of all the odd numbers and the sum of all the even numbers from the list and print them out. 
"""
numbers=int(input("Enter range of list of number:"))
list_of_number=[]
sum_of_odd=0
for i in range(numbers):
    list_num=int(input(f"Enter {i+1} number:"))
    list_of_number.append(list_num)
    if list_num%2!=0:
        sum_of_odd+=list_num
print(f"Sum of odd number in {list_of_number} is {sum_of_odd}")