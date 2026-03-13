'''
    Exercise 7: Abstract Base Classes - Payment System
    
    Haven't implemented cryptoprocessor
'''

from abc import ABC, abstractmethod
import datetime as dt
import logging

logging.basicConfig(filename='transactions.log')

def PaymentProcessor(ABC):
    '''
        Abstract base class for payment classes: credit card, paypal, crypto
    '''
    logger = logging.getLogger(__name__) 
    
    @abstractmethod
    def validate(self):
        pass
    
    @abstractmethod
    def process_payment(self,amount):
        pass
    
    @abstractmethod
    def refund(self,transaction_id):
        pass
    
    def log_transaction(self,details,level):
        '''
            A method to log the details of a transaction along with the log level
        '''
        if details is not None:
            logger.log(level,details)
    

class CreditCardProcessor(PaymentProcessor):
    '''
        Child class of Payment Processor
        Simulates credit card payment processing - kind of
    '''
    def __init__(self,credit_card_no):
        self.credit_card_no = credit_card_no
        self.transactions = {} #a store of all the transactions made so far in the format `transac_id:amount`
        
    def validate(self):
        '''
            Checks if credit card is genuine by checking the length of no
            Returns True if genuine otherwise False
        '''
        if len(self.credit_card_no) != 16:
            return False
        return True
    
    def process_payment(self,amount):
        '''
            Validates user card, takes in the amount, generates a transaction id, add it to transaction dict and logs each process
        '''
        self.log_transaction(f"""Initiating card payment for credit card {self.credit_card_no}.\n
                                Time: {dt.datetime.now()}
                                Amount: {amount}\n""",logging.INFO)
        
        if not self.validate():
            self.log_transaction(f"Invalid card details.\nTransaction failed",logging.ERROR)
            return
        
        transac_id = 'TXCrC' + str(dt.datetime.now()) + str(len(self.transactions) + 100) #looks something like TXCrC2029-03-11101
        self.transactions[transac_id] = amount
        
        self.log_transaction(f"Transaction successfull\nTransaction id: {transac_id}",logging.INFO)
        
        return transac_id
    
    def refund(self,transaction_id):
        '''
            Checks for valid transac id, and pops transaction from the dict on refund
            Logs the process
        '''
        self.log_transaction(f"""Initiating refund of transaction id {transaction_id}.\n
                                Time: {dt.datetime.now()}""",logging.INFO)
        
        if not transaction_id in self.transactions.keys():
            self.log_transaction(f"Invalid transaction details.\nRefund failed",logging.ERROR)
            return
        
        del self.transactions[transaction_id]
        
        self.log_transaction(f"Refund of transaction id: {transaction_id} successfull",logging.INFO)
        

class PaypalProcessor(PaymentProcessor):
    '''
        Child class of Payment Processor
        Simulates paypal payment processing - kind of
    '''
    transac_limit = 50000 
    
    def __init__(self,card):
        self.card = card #takes in a card instance (could be credit/debit), even though we have defined a credit card class only
        self.transactions = {} #a store of all the transactions made so far in the format `transac_id:bank_transac_id`
        
    def validate(self):
        '''
            Checks if card is genuine
            Returns True if genuine otherwise False
        '''
        if not self.card.validate():
            return False
        return True
    
    def process_payment(self,amount):
        '''
            Validates user card, takes in the amount, generates a transaction id, initiates the card payment, adds it to transaction dict and logs each process
        '''
        self.log_transaction(f"""Initiating paypal payment for card {self.card.credit_card_no}.\n 
                                Time: {dt.datetime.now()} 
                                Amount: {amount}\n""",logging.INFO) #have taken credit card here, even though it should change according to card type
        
        if not self.validate():
            self.log_transaction(f"Invalid card details.\nTransaction failed",logging.ERROR)
            return
        
        if amount > PaypalProcessor.transac_limit:
            self.log_transaction(f"Transaction limit is set to {PaypalProcessor.transac_limit}.\nTransaction failed",logging.ERROR)
            return
        
        transac_id = 'TXPPL' + str(dt.datetime.now()) + str(len(self.transactions) + 100) #looks something like TXPPL2029-03-11101
        bank_transac_id = self.card.process_payment(amount)
        self.transactions[transac_id] = bank_transac_id
        
        self.log_transaction(f"Transaction successfull\nTransaction id: {transac_id}",logging.INFO)
        
        return transac_id
    
    def refund(self,transaction_id):
        '''
            Checks for valid transac id, and pops transaction from the dict on refund
            Logs the process
        '''
        self.log_transaction(f"""Initiating refund of transaction id {transaction_id}.\n
                                Time: {dt.datetime.now()}""",logging.INFO)
        
        if not transaction_id in self.transactions.keys():
            self.log_transaction(f"Invalid transaction details.\nRefund failed",logging.ERROR)
            return
        
        if self.card.refund(): #Why `not`` is not used? On failure, refund() returns 'return', which is truthy. On success, refund() returns None, which is falsy.
            self.log_transaction(f"Refund failed on the bank end. Kindly contact your bank.",logging.ERROR)
            return
        
        del self.transactions[transaction_id]
        
        self.log_transaction(f"Refund of transaction id: {transaction_id} successfull",logging.INFO)
        
