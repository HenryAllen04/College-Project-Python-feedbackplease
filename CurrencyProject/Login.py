username_requirements = ('''Username requirements:\n
                    Username should not already be in use.\n
                    Username should not contain any digits.\n
                    Username should not have more than 10 characters.\n
                    Username should have more than 4 characters.\n
                    Example: your first name and last name :) \n''')

passwd_requirements = ('''Password requirements:\n
                    Password length should be at least 6 characters.\n
                    Password length should not be greater than 12 characters.\n
                    Password should have at least 1 numeral.\n
                    Password should have at least 1 uppercase.\n
                    Password should have at least 1 lowercase.\n
                    Password should contain 1 of these symbols $@#.\n

                    Example: P10ot$yum''')

def view_requirements():
    print()
    choice = input("would you like to view the\n-username and password requirements-\n(Y/N) =:")
    choice = choice.upper()
    val = False
    if choice == ('Y'):
        val = True
       # print("/n")
        
        print(username_requirements)
       # print()
       
        print(passwd_requirements)
        #print()
        
    if choice == ('N'):
        val = True
        
    elif val == False:
        #print()
        print("!please answer (Y/N!")
        view_requirements()

# Function to validate the password
def password_check(passwd):
      
    SpecialSym =['$', '@', '#', '%']
    val = True
      
    if len(passwd) < 6: #if the password is less than 6
        print('length should be at least 6')
        val = False
          
    if len(passwd) > 12: #if the password is greater than 8
        print('length should be not be greater than 12')
        val = False
          
    if not any(char.isdigit() for char in passwd): #if there are no characters in the password with a digit
        print('Password should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in passwd): #if there are no uppercase letters
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in passwd): #if there are no lowercase letters
        print('Password should have at least one lowercase letter')
        val = False
          
    if not any(char in SpecialSym for char in passwd): #if there are no special symbols
        print('Password should have at least one of the symbols $@#%')
        val = False
    if val:         #This means if true or false because the variable val is true or false
        return val

def username_back_check(username):
    existing_users = open("BankLoginData.txt", "r").read().split("\n") #"r" will open the txt in a read mode and .read() will read the txt file

    try:
        for datarow in existing_users:
            line = datarow.split("-") #This has split details into a formatted list to check do print(line)
            user_name = line[0] #this will pull column 0 out of a line which is username data
            
            if user_name == username:
                print("username already in use \n account not created")
                print()
                start_choice()
                
    except IndexError:
        print("no existing users in database")

#Username Check function
def username_check(username):

    val = True
    
    if username_back_check(username):
        val = False

    if any (char.isdigit() for char in username):
        print("Username should not contain any digits")
        val = False

    if len(username) > 10:
        print("Username is too long")
        val = False

    if len(username) < 4:
        print("Username is too short")
        val = False
    if val:
        return val

def filewrite_create_account(username, passwd):
    f = open("BankLoginData.txt", "a")
    f.write(username)
    f.write("-")
    f.write(passwd)
    f.write("\n")
    f.close()
    print()
    print("Your account has been created")
    print()

# Creating a new account
def create_account():
    view_requirements()

    username = input("Enter your desired username: ").strip()# this will get rid of any spaces
    passwd = input("enter your desired password: ")
    val = True
    
    if (username_check(username)):
        print("Username accepted")
    else:
        print("Username not accepted, please enter a valid username!")
        val = False
        create_account()
      
    if (password_check(passwd)):   #if the val is = True 
        print("Password accepted")
    else:                             #if the val is = False
        print("Password not accepted, please enter a valid password when creating an account")
        val = False
        create_account()
    if val:
        filewrite_create_account(username, passwd) #passing through variables username and passwd
        print("You are logged into your new account :) ")
        


def login_check(user_name_input, user_passwd_input):
    existing_users = open("BankLoginData.txt", "r").read().split("\n") #"r" will open the txt in a read mode and .read() will read the txt file

    try:
        for datarow in existing_users:
            line = datarow.split("-") #This has split details into a formatted list to check do print(line)
            user_name = line[0] #this will pull column 0 out of a line which is username data
            user_passwd = line[1] #this will pull column 1 out of a line which is password data
  
            if user_name == user_name_input and user_passwd == user_passwd_input:
                return True
            else:
                return False
    except IndexError:
        print("no existing users in database")


def account_login():
    user_name_input = input("Please enter the username to your account: ")
    user_passwd_input = input("Please enter the password to your account: ")
    

    if (login_check(user_name_input, user_passwd_input)): #this passes the variables into the top function
        print("login successful")
        print()
    else:
        print("login not successful \n please try again!")
        print()
        start_choice()
        


def start_choice():
    print("1-create a account \n2-login to account ")
    choice = int(input("Enter number: "))
    if choice == 1:
        create_account()
    if choice == 2:
        account_login()
        # ADD code to if input didnt equal 2 or 1
