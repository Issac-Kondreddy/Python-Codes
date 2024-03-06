class BankAccount:

    def __init__(self, AccountNumber, Balance):
        self._AccountNumber = AccountNumber
        self.__Balance = Balance

    def deposit(self,amount):
        if amount>0:
            self.__balance += amount
            print(f"Balance deposited of amount {amount}")

    def withdraw(self,amount):
        if 0<amount<=self.__Balance:
            self.__Balance -=amount
            print(f"Withdrew {amount} from the account")
        else:
            print("Insufficient balance or invalid amount")

    def get_Balance(self):
        return self.__Balance

    def set_Balance(self, amount):
        if not isinstance(amount, int):
            raise ValueError("Balance must be a number")
        self.__Balance = amount

    balance = property(get_Balance, set_Balance)


BankAccount = BankAccount(11223454, 25000)
print(BankAccount.balance)
BankAccount.set_Balance(45000)
print(BankAccount.balance)


