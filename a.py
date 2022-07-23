class ATM:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 50000")

    def withdrawl(self,amount):
        new_amount = 50000 - amount
        print("You have withdrawl amount "+str(amount) +
        ". Your remaining balance is "+ str(new_amount))

def main():
    Card_number = input("insert your card number:-  ")
    pin_number = input("enter your pin number:-  ")

    new_user = ATM(Card_number ,pin_number)

    print("Choose your activity  ")
    print("1. BALANCE ENQUIRE    2.WITHDRAWL")
    activity = int(input("Enter activity number:-  "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input(" Enter the amount:-  "))
        new_user.withdrawl(amount)
    else:
        print("Enter a valid number")

main()