import random
one_set=set()
another_set=set()
list_of_set=[one_set,another_set]
for choosen_set in list_of_set:
    try:
        no_of_values=int(input(f"Enter no. of value for {choosen_set}:"))
    except ValueError as e:
        print(f"Value error of {e} so taking random number as input")
        no_of_values=random.randint(1,10)
    for i in range(1,no_of_values+1):
        choosen_set.add(int(input(f"Enter {i} number:")))
print(f"Intersection between {list_of_set} is {one_set.intersection(another_set)}")
print(f"Union between {list_of_set} is {one_set.union(another_set)}")