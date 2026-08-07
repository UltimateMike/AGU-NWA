import time

Balance = 50000
UserPin = 2255


def UserInput(): 
    UserPinInput = int(input(f"Please enter your pin to continue::\n"))
    if UserPinInput == UserPin: 
        time.sleep(2)
        print(":::Welcome To Ultimate Micro Finance Bank:::")
        BankOperations()
    elif UserPinInput is not UserPin:
         time.sleep(2)
         print("Incorrect pin,please try again")
         UserInput()
         
         
def BankOperations():
    userInput = int(input("What would you like to do?\n1.Check Balance\n2Deposit\n3.Withdraw\n4.Exit\n"))
    if userInput == 1:
        CheckBalance()
    elif userInput == 2:
        Deposit()
    elif userInput == 3:
        Withdraw()
    elif userInput == 4: 
        exit()
        
def CheckBalance():
        print("Please Wait::::::::::::")
        time.sleep(2)
        print(Balance)
        AnotherTransaction()
            
def Deposit():
        userInput = int(input("How much would you like to deposit?\n"))
        totalBalance = userInput + Balance
        print("Processing...")
        time.sleep(2)
        print(f"Deposit Successful\n Your New Account Balance is {totalBalance}")
        AnotherTransaction()
                 
                 
def Withdraw():
    global Balance
    amount = float(input("enter amount to withdrawn"))
    if amount <= 0:
        print("please enter a valid amount.")
    elif  amount <= Balance:
        Balance = Balance - amount 
        print("withdrawal successful")
        print("Remaining Balance:", Balance)
    else:
        print("Insufficient funds")
    AnotherTransaction()
        
def AnotherTransaction():
    userInput = int(input("Will you like to do another Transaction?\n1.Yes\n2.No\n"))
    if userInput == 1:
        BankOperations()
    elif userInput == 2:
        Exit()
        
def Exit():
    print(":::::::::::::THANK YOU FOR BANKING WITH US:::::::::::::::")
                 
    
UserInput()