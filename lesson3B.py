class Account:
    def __init__(self,account_type):
        self.account_type =account_type

    def check_balance(self, balance):
       return f"your balance is {balance}  {self.account_type}"

    def withdraw(self):
        return "This is Withdraw function "

account_instance = Account('savings')
account_instance.account_type='savings'

print(account_instance.check_balance(3000))
current_account = Account('current')
current_account.account_type= 'current'

print(account_instance.check_balance(4000))

