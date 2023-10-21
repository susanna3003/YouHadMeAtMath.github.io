# Import modules
import time

# All accounts
users = {
    "root": {
        "password": "gucci-mane",
        "group": "admin",
        "math problem": []
    }
}

# Form validation
def validate(form):
    if len(form) > 0:
        return False
    return True

# Login authorization
def loginauth(username, password):
    if username in users:
        if password == users[username]["password"]:
            print("Login successful")
            return True
    return False

# Login
def login():
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("Username can't be blank")
        else:
            break
    while True:
        password = input("Password: ")
        if not len(password) > 0:
            print("Password can't be blank")
        else:
            break

    if loginauth(username, password):
        return session(username)
    else:
        print("Invalid username or password")

# Register
def register():
    while True:
        username = input("New username: ")
        if not len(username) > 0:
            print("Username can't be blank")
            continue
        if username in users:
            print("Username already exists")
            continue
        else:
            break
    while True:
        password = input("New password: ")
        if not len(password) > 0:
            print("Password can't be blank")
            continue
        if username in password:
            print("Password has/is already being used")
            continue
        else:
            break
    while True:
        accountTy = input("Type of account: student/kid or teacher/parent: ")
        if not len(accountTy) > 0:
            print("Please pick the type of account")
            continue
        else:
            break 
    print("Creating account...")
    users[username] = {}
    users[username]["password"] = password
    users[username]["group"] = "user"
    users[username]["math problem"] = []
    time.sleep(1)
    print("Account has been created")

# Send mail
def sendmail(username):
    while True:
        recipient = input("Recipient > ")
        if not len(recipient) > 0:
            print("Recipient can't be blank")
            continue
        elif recipient not in users:
            print("There is no account with that username")
            continue
        else:
            break
    while True:
        subject = input("Subject > ")
        if not len(subject) > 0:
            print("Subject can't be blank")
            continue
        else:
            break
    while True:
        context = input("Context > ")
        if not len(context) > 0:
            print("Context can't be blank")
        else:
            break
    print("Sending math...")
    users[recipient]["math"].append(["Sender: " + username, "Subject: " + subject, "Context: " + context])
    time.sleep(1)
    print("Mail has been sent to " + recipient)

# User session
def session(username):
    print("Welcome to your account " + username)
    print("Options: view math problems | MATH/send mail | logout")
    if users[username]["group"] == "admin":
        print("")
    while True:
        option = input(username + " > ")
        if option == "logout":
            print("Logging out...")
            break
        elif option == "view math problems":
            print("Current Math Problem:")
            for mathPao in users[username]["math problems"]:
                print(mathPao)
        elif option == "MATH/send mail":
            sendmail(username)
        elif users[username]["group"] == "admin":
            if option == "users' math problems":
                print("Whos math problems would you like to see?")
                userinfo = input("> ")
                if userinfo in users:
                    for mathPao in users[userinfo]["math problems"]:
                        print(mathPao)
                else:
                    print("There is no account with that username")
            elif option == "delete math problems":
                print("Whos math problems would you like to delete?")
                userinfo = input("> ")
                if userinfo in users:
                    print("Deleting " + userinfo + "'s math problems...")
                    users[userinfo]["math problems"] = []
                    time.sleep(1)
                    print(userinfo + "'s math problems has been deleted")
                else:
                    print("There is no account with that username")
            elif option == "delete account":
                print("Whos account would you like to delete?")
                userinfo = input("> ")
                if userinfo in users:
                    print("Are you sure you want to delete " + userinfo + "'s account?")
                    print("Options: yes | no")
                    while True:
                        confirm = input("> ")
                        if confirm == "yes":
                            print("Deleting " + userinfo + "'s account...")
                            del users[userinfo]
                            time.sleep(1)
                            print(userinfo + "'s account has been deleted")
                            break
                        elif confirm == "no":
                            print("Canceling account deletion...")
                            time.sleep(1)
                            print("Account deletion canceled")
                            break
                        else:
                            print(confirm + " is not an option")
                else:
                    print("There is no account with that username")
        else:
            print(option + " is not an option")

# On start
print("Welcome to the system. Please register or login.")
print("Options: register | login | exit")
while True:
    option = input("> ")
    if option == "login":
        login()
    elif option == "register":
        register()
    elif option == "exit":
        break
    else:
        print(option + " is not an option")

# On exit
print("Shutting down...")
time.sleep(1)
