import random
class atm:
    def __init__(self,card_number,pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
    def CashWithdrawal():
        amt=input("Amount to be withdrawn:")
        pin_number=input("PIN number:")
        print("CAsh Withdrawn..")
    def balanceEnquiry():
        balance=str(random.randint(0,10000000))
        print("You have Rs."+balance+" in your account")
    CashWithdrawal()
    balanceEnquiry()

        