import re,os,hashlib
class User:
    _key=4
    def __init__(self):
        print("User Instance")
    def User_registration(self):
        name=input("Enter user name:")
        password=input("Enter password:")
        check_password=self.validatePassword(password)
        hash_password=''
        if check_password:
            current_dir=os.path.dirname(os.path.abspath(__file__))
            file=open(current_dir+'/user.txt','a')
            for p in password:
                hash_password+=chr(ord(p)+self._key)
            user_dict={'username':name,'password':hash_password}
            file.write(str(user_dict)+'\n')
            file.close()
        else:
            print("Password Invalid!Try Again")
    def checkUser(self):
        name=input("Enter user name:")
        user_found=False
        current_dir=os.path.dirname(os.path.abspath(__file__))
        file=open(current_dir+'/user.txt','r')
        for f in file:
            user_val=eval(f.strip())
            if user_val['username']==name:
                user_found=True
                break
        if user_found:
            print(f"User is Registered")
        else:
            print(f"User is not Registered")
    def validatePassword(self,password):
        password_pattern=r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
        if re.match(password_pattern,password):
            return True
        else:
            return False
    def login(self):
        name=input("Enter user name:")
        password=input("Enter password:")
        user_login_sucessful=False
        hash_password=''
        for p in password:
                hash_password+=chr(ord(p)+self._key)
        current_dir=os.path.dirname(os.path.abspath(__file__))
        file=open(current_dir+'/user.txt','r')
        for f in file:
            user_val=eval(f.strip())
            if user_val['username']==name and user_val['password']==hash_password:
                user_login_sucessful=True
                break
        if user_login_sucessful:
            print(f"User sucessfully Logged in")
        else:
            print(f"Enter correct username or password")
usr=User()
while 1:
    choice=input("Enter command [register,check,login,exit]:")
    match choice:
        case 'register':
            usr.User_registration()
        case 'check':
            usr.checkUser()
        case 'login':
            usr.login()
        case 'exit':
            choice=input("Are you sure you want to exit[yes/no]:").lower()
            if choice=='yes' or choice=='y':
                del usr
                break
            else:
                print("Continuing....")
        case default:
            print("Enter Valid command")