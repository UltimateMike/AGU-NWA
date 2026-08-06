import time

# Initial state
Balance = 50000
UserPin = 2255

def show_loading(message="Processing"):
    #Uses a for loop to display a visual loading dot animation.
    print(message, end="", flush=True)
    for _ in range(60):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

def UserInput(): 
    """Handles PIN authentication using a while loop."""
    attempts = 3
    
    while attempts > 0:
        try:
            UserPinInput = int(input("Please enter your PIN to continue:\n"))
            if UserPinInput == UserPin:
                show_loading("Authenticating")
                print("::: Welcome To Ultimate Micro Finance Bank :::\n")
                BankOperations()
                return  # Exit function after completion
            else:
                attempts -= 1
                show_loading("Verifying")
                if attempts > 0:
                    print(f"Incorrect PIN. You have {attempts} attempt(s) left.\n")
                else:
                    print("Too many incorrect attempts. Account locked.")
                    return
        except ValueError:
            print("Invalid input. Please enter numeric digits only.\n")

def BankOperations():
    """Main menu loop."""
    while True:
        print("\nWhat would you like to do?")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        try:
            userInput = int(input("Select an option (1-4): "))
            if userInput == 1:
                CheckBalance()
                break
            elif userInput == 2:
                Deposit()
                break
            elif userInput == 3:
                Withdraw()
                break
            elif userInput == 4: 
                Exit()
                break
            else:
                print("Invalid selection. Please choose options 1 to 4.")
        except ValueError:
            print("Please enter a valid number.")

def CheckBalance():
    show_loading("Retrieving account details")
    print(f"Your Current Balance is: ${Balance:,.2f}\n")
    AnotherTransaction()
            
def Deposit():
    global Balance
    
    while True:
        try:
            userInput = float(input("How much would you like to deposit?\n$"))
            if userInput <= 0:
                print("Deposit amount must be greater than zero.")
                continue
                
            Balance += userInput
            show_loading("Processing Deposit")
            print("Deposit Successful!")
            print(f"Your New Account Balance is: ${Balance:,.2f}\n")
            AnotherTransaction()
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
                 
def Withdraw():
    global Balance
    
    while True:
        try:
            userWithdraw = float(input("How much do you want to withdraw?\n$"))
            if userWithdraw <= 0:
                print("Withdrawal amount must be greater than zero.")
                continue
                
            if userWithdraw > Balance:
                show_loading("Verifying Funds")
                print("Insufficient Funds! Please enter a lower amount.\n")
            else:
                Balance -= userWithdraw
                show_loading("Dispensing Cash")
                print("Withdrawal Successful!")
                print(f"Remaining Balance: ${Balance:,.2f}\n")
                AnotherTransaction()
                break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
        
def AnotherTransaction():
    while True:
        try:
            userInput = int(input("Would you like to do another transaction?\n1. Yes\n2. No\nSelect: "))
            if userInput == 1:
                BankOperations()
                break
            elif userInput == 2:
                Exit()
                break
            else:
                print("Please enter 1 for Yes or 2 for No.")
        except ValueError:
            print("Invalid entry. Please type 1 or 2.")
        
def Exit():
    print("\n" + "=" * 50)
    print("   THANK YOU FOR BANKING WITH ULTIMATE MICROFINANCE   ")
    print("=" * 50)

# Start the application
UserInput()