class Account:
    def __init__(self,account_type):
        self.account_type =account_type

    def check_balance(self):
        print("Account balance is")


    #    return f"your balance is {balance}  {self.account_type}"

    def withdraw(self):
        return "This is Withdraw function "

    def save(self):
        return "This is save function"


account_instance = Account
account_instance.account_type="savings"
account_instance.account_type="fixed"

instance_account_type = account_instance.account_type
print(instance_account_type)
account_instance.check_balance()
