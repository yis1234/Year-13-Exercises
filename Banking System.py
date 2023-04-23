class User:
    def __init__(self, first_name, last_name, gender, street_address, city, email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        userList.append(self)
    
    def displayInfo(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Gender: {self.gender}")
        print(f"Street Address: {self.street_address}")
        print(f"City: {self.city}")
        print(f"Email: {self.email}")
        print(f"Credit Card Number: {self.cc_number}")
        print(f"Credit Card Type: {self.cc_type}")
        print(f"Balance: {self.balance}")
        print(f"Account Number: {self.account_no}")

        
def generateUsers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], float(line[8]), line[9])

def findUser():
    firstname = input("Enter User First Name: ").title()
    lastname = input("Enter User Last Name: ").title()
    for user in userList:
        if user.first_name == firstname and user.last_name == lastname:
            user.displayInfo()
            break
    else:
        print("User not found")

    True
    
def overdrafts():
    count = 0
    total_overdraft = 0
    for user in userList:
        if user.balance < 0:
            print(f"{user.first_name} {user.last_name} has an overdraft balance of {user.balance}")
            count += 1
            total_overdraft += user.balance
    print(f"{count} users have an overdraft balance")
    print(f"Total Overdrafts: {total_overdraft:,.2f}")
    

    True
    
def missingEmails():
    count = 0
    for user in userList:
        if user.email == "":
            print(f"{user.first_name} {user.last_name} doesn't have an email address")
            count += 1
    print(f"{count} don't have email addresses")

    True

def bankDetails():
    print(f"There are {len(userList)} users")
    total_balance = 0
    for user in userList:
        total_balance += user.balance
    print(f"Total Balance: ${total_balance:,.2f}")
    # print the user and the balance of the person with highest balance
    for user in userList:
        if user.balance == max(userList, key=lambda x: x.balance).balance:
            print(f"{user.first_name} {user.last_name} has the highest balance of ${user.balance:,.2f}")
        elif user.balance == min(userList, key=lambda x: x.balance).balance:
            print(f"{user.first_name} {user.last_name} has the lowest balance of ${user.balance:,.2f}")


    True
    
def transfer():
    acc = input("Enter Account Number: ")
    for user in userList:
        if user.account_no == acc:
            print(f"First Name: {user.first_name}")
            print(f"Last Name: {user.last_name}")
            print(f"Balance: ${user.balance:,.2f}")
            transfer = float(input("Enter Amount to Transfer: "))
            firstname = user.first_name
            lastname = user.last_name
            balance = user.balance
            if transfer > user.balance:
                print("Insufficient Funds")
            else:
                balance -= float(transfer)
                user2 = input("Enter Account Number to transfer to: ")
                # print that user 1 including first name and last name has transferred to user 2 with first name and last name of both users
                for user in userList:
                    if user.account_no == user2:
                        user.balance += float(transfer)
                        print(f"{firstname} {lastname} has transferred ${transfer:,.2f} to {user.first_name} {user.last_name}")
                        print(f"{firstname} {lastname} has ${balance:,.2f}")
                        print(f"{user.first_name} {user.last_name} has ${user.balance:,.2f}")

                
    True

userList = []          
generateUsers()

userChoice = ""
print("Welcome")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ")
    print()
    
    if userChoice == "1":
        findUser()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missingEmails()
    elif userChoice == "4":
        bankDetails()
    elif userChoice == "5":
        transfer()      