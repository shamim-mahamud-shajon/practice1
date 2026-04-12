class Bank:
    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value > 0:
            self.__balance = value

b = Bank()
b.balance = 1000
print(b.balance)