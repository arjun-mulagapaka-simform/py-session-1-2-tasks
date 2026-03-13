'''
    Exercise 5: OOP - Banking System
'''

import logging
logger = logging.getLogger(__name__)    

def transac_logger(func):
    '''
        Decorator to log all transactions
    '''
    def wrapper(*args,**kwargs):
        self = args[0] #the calling object
        amount = args[1] #transaction amount
        acc_no = self.get_account_no() #caller's account no
        
        logging.basicConfig(filename='transactions.log', level=logging.INFO)
        
        match func.__name__:
            case 'deposit':
                logger.info(f"Initiated deposit of {amount} in account {acc_no}")
                try:
                    func(*args,**kwargs)
                except Exception as e:
                    logger.error(f"Ran into error: {e} while depositing {amount} in account {acc_no}")
                else:
                    logger.info(f"Deposit of {amount} completed in account {acc_no}")
            case 'withdraw':
                logger.info(f"Initiated withdrawal of {amount} from account {acc_no}")
                try:
                    func(*args,**kwargs)
                except Exception as e:
                    logger.error(f"Ran into error: {e} while withdrawing {amount} from account {acc_no}")
                else:
                    logger.info(f"Withdrawal of {amount} completed from account {acc_no}")
            case 'tranfer':
                acc_2 = args[2].get_account_no()
                logger.info(f"Initiated transfer of {amount} from account {acc_no} to account {acc_2}")
                try:
                    func(*args,**kwargs)
                except Exception as e:
                    logger.error(f"Ran into error: {e} while transferring {amount} money from account {acc_no} to account {acc_2}")
                else:
                    logger.info(f"Transfer of {amount} completed from account {acc_no} to account {acc_no}")
            case _:
                logger.error("Something unexpected happened with the system")
        
    return wrapper

class InsufficientFundsError(Exception):
    '''
        Custom exception class for a scenario where funds are insufficient
    '''
    def __init__ (self, message="Insufficient funds"):
        self.message = message
        super().__init__(self.message)

class InvalidTransactionError(Exception):
    '''
        Custom exception class for a scenario where transaction properties are invalid
    '''
    def __init__ (self, message="Invalid transaction"):
        self.message = message
        super().__init__(self.message)

class Account:
    '''
        Base class for all accounts
        Contains info: 
            account_count and total_balance at class level
            acc_no, balance and owner at object level
    '''
    account_count = 0 #account no. is a class variable cos it is controlled centrally
    total_balance = 0
    
    def __init__(self,balance,owner):
        self.balance = balance
        self.owner = owner
        Account.account_count += 1 
        self.__account_number = "MKAHM" + str(Account.account_count)
        
        Account.total_balance += self.balance
    
    def get_account_no (self):
        return self.__account_number
    
    @transac_logger
    def deposit(self,amount):
        '''
            Deposits amount in the account
        '''
        self.balance += amount
        Account.total_balance += amount
    
    @transac_logger
    def withdraw(self,amount):
        '''
            Withdraws specified amount from current account
            Checks for sufficient balance
        '''
        if amount > self.balance:
            raise InsufficientFundsError
        
        self.balance -= amount
        Account.total_balance -= amount
        
    @transac_logger
    def transfer(self,amount,receiver_account):
        '''
            Transfers specified amount from current account to specified receiver account
            Calls withdraw function for current account and deposit for receiver account
        '''
        if receiver_account is None:
            raise InvalidTransactionError("Invalid receiver account")
        
        self.withdraw(amount)
        receiver_account.deposit(amount)
        
    @classmethod
    def get_total_balance(cls):
        '''
            Returns the total balance of all the accounts in the bank
        '''
        return Account.total_balance
        
class SavingsAccount(Account):
    '''
        A child class of Account which manages accounts with a plus of interest rate and min balance
    '''
    interest_rate = 0.6 #default interest rate for savings account
    minimum_required_balance = 2000 #required min balance for savings account
    
    def __init__(self, balance, owner):
        if balance < self.minimum_required_balance:
            raise InvalidTransactionError("Account creation not possible due to initial balance not meeting minimum balance requirements")
        super().__init__(balance, owner)
        
    @transac_logger
    def withdraw(self, amount):
        '''
            Overrides base function to add the constraint of min balance during withdrawal
        '''
        if (self.balance - amount) < SavingsAccount.minimum_required_balance:
            raise InsufficientFundsError("Cannot withdraw funds due to minimum balance requirements")
        return super().withdraw(amount)

class CheckingAccount(Account):
    '''
        A child class of Account which behaves like an overdraft account
    '''
    overdraft_limit = 50000 #overdraft is similar to leverage
    
    def __init__(self, balance, owner):
        super().__init__(balance, owner)
        
    @transac_logger
    def withdraw(self, amount):
        '''
            Overrides base function to add the constraint of overdraft limit during withdrawal
        '''     
        if self.balance > amount:
            return super().withdraw(amount)
        else:
            if abs(self.balance - amount) > CheckingAccount.overdraft_limit:
                raise InsufficientFundsError("You cannot cross your overdraft limit!")
    
if __name__ == "__main__":
    # accounts = {}  # Dictionary to store accounts with account_no as key

    # print("=== Welcome to AHM Bank ===")

    # while True:
    #     print("\nWhat would you like to do today?")
    #     print("1. Create Savings Account")
    #     print("2. Create Checking Account")
    #     print("3. Deposit Money")
    #     print("4. Withdraw Money")
    #     print("5. Transfer Money")
    #     print("6. Show Account Balance")
    #     print("7. Show Total Bank Balance")
    #     print("8. Exit")

    #     choice = input("Enter your choice (1-8): ").strip()

    #     try:
    #         if choice == '1':
    #             owner = input("Enter your name: ").strip()
    #             balance = int(input(f"Enter initial balance (minimum {SavingsAccount.minimum_required_balance}): "))
    #             account = SavingsAccount(balance, owner)
    #             accounts[account.get_account_no()] = account
    #             print(f"🎉 Savings account created! Account number: {account.get_account_no()}")

    #         elif choice == '2':
    #             owner = input("Enter your name: ").strip()
    #             balance = int(input("Enter initial balance: "))
    #             account = CheckingAccount(balance, owner)
    #             accounts[account.get_account_no()] = account
    #             print(f"🎉 Checking account created! Account number: {account.get_account_no()}")

    #         elif choice == '3':
    #             acc_no = input("Enter your account number: ").strip()
    #             if acc_no not in accounts:
    #                 print("❌ Account not found!")
    #                 continue
    #             amount = int(input("Enter amount to deposit: "))
    #             accounts[acc_no].deposit(amount)
    #             print(f"✅ Deposit successful! New balance: {accounts[acc_no].balance}")

    #         elif choice == '4':
    #             acc_no = input("Enter your account number: ").strip()
    #             if acc_no not in accounts:
    #                 print("❌ Account not found!")
    #                 continue
    #             amount = int(input("Enter amount to withdraw: "))
    #             accounts[acc_no].withdraw(amount)
    #             print(f"✅ Withdrawal complete! New balance: {accounts[acc_no].balance}")

    #         elif choice == '5':
    #             sender_no = input("Enter your account number: ").strip()
    #             receiver_no = input("Enter receiver's account number: ").strip()

    #             if sender_no not in accounts or receiver_no not in accounts:
    #                 print("❌ One or both accounts not found!")
    #                 continue

    #             amount = int(input("Enter amount to transfer: "))
    #             accounts[sender_no].transfer(amount, accounts[receiver_no])
    #             print(f"✅ Transfer successful! Your new balance: {accounts[sender_no].balance}")

    #         elif choice == '6':
    #             acc_no = input("Enter your account number: ").strip()
    #             if acc_no not in accounts:
    #                 print("❌ Account not found!")
    #                 continue
    #             account = accounts[acc_no]
    #             print(f"💰 Account Balance for {acc_no} ({account.owner}): {account.balance}")

    #         elif choice == '7':
    #             print(f"🏦 Total bank balance across all accounts: {Account.get_total_balance()}")

    #         elif choice == '8':
    #             print("👋 Thank you for banking with AHM Bank. Goodbye!")
    #             break

    #         else:
    #             print("❌ Invalid choice! Please enter a number between 1 and 8.")

    #     except InsufficientFundsError as e:
    #         print(f"⚠️ Transaction failed: {e}")
    #     except InvalidTransactionError as e:
    #         print(f"⚠️ Transaction failed: {e}")
    #     except ValueError:
    #         print("⚠️ Invalid input! Please enter numeric values for amounts.")