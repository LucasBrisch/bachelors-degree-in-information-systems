import json


def login():
    print ("Login")
    username = input("Username: ")
    password = input("Password: ")
    
    with open ('users.json', "r") as file:
        users = json.loads(file.read())
        
        for user in users:
            if user["username"] == username and user["password"] == password:
                print("Login successful")
                return

        print("Invalid user or password")
        login()


def register():
    print ("Register")
    username = input("Username: ")
    if user_exists(username):
        print ("User already exists")
        register()
    else:
        password = input("Password: ")
        password2 = input("Confirm Password: ")
        if password == password2:
            User_to_database(username, password)
        else:
            print ("Password does not match")
            register()
        
        
def user_exists(username):
    
    with open("users.json", "r") as file:
        
        users = json.load(file)
        return username in users


def User_to_database(username, password):
    with open ('users.json', "r") as file:
        users = json.loads(file.read())
    
    
    with open("users.json", "w") as file:
        
        
        
        users.append({"username": username, "password": password})      
        
        file.write(json.dumps(users))
        
        print ("User registered")

    


def main():
    
    print ("1 - login")
    print ("2 - register")
    
    option = input("Choose an option: ")
    if option == "1":
        login()
    elif option == "2":
        register()
        
        
main()