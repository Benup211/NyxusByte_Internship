class Car_Racing:
    _car_state=['stop','start']
    def __init__(self):
        print(f"{'Avaliable command in Car Racing':*^50}")
        print(f"{'start->start the car':-^50}")
        print(f"{'stop->stop the car':-^50}")
        print(f"{'exit->exit the program':-^50}")
        print("*"*50)
    def car_command(self,command):
        del_obj=False
        if (command==self._car_state[0]):
            print(f"Car is already in {self._car_state[0]} state")
        elif (command=="exit"):
            print("Are you sure you want to exit?")
            choice=input("Enter [yes,no]:").lower()
            if (choice =='yes' or choice=='y'):
                del_obj=True
            else:
                print("Continuing....")
        elif (command==self._car_state[1]):
            self._car_state.reverse()
            print(f"Car is changed to {self._car_state[0]} state")
        else:
            print("Command not avaliable!Try Again")
        return del_obj
my_car=Car_Racing()
while(True):
    user_command=input("Enter your command[start,stop,exit]:")
    if (my_car.car_command(user_command)):
        print("Exiting the program")
        del my_car
        break