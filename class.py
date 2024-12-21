class BankAccount:
    def __init__(self, owner, balance=0):
        self._owner = owner
        self._balance = balance

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        raise AttributeError("Нельзя изменить владельца счёта")

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self._balance = value

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount


account = BankAccount("Ислам", 200)

print("welcome our  bank")
while True:
    x = input("Выберите действие \n"
              "1 -> О моем счете \n"
              "2 -> Пополнение счёта \n"
              "3 -> Снятие денег \n"
              "4 -> Выход \n")
    """ Пополнение счёта """
    if x == "1":
        print(f"Владелец счёта: {account.owner}")
        print(f"Начальный баланс: {account.balance}", end="$\n")
    elif x == "2":
        while True:
            d = int(input("Пополнение счёта\n"
                          "--> ведите сумму :"))
            if d < 0:
                print("Сумма пополнения должна быть положительной")
            else:
                account.deposit(d)
                print(f"Баланс: {account.balance}", end="$\n")
                break
    elif x == "3":
        """ Снятие денег """
        while True:
            d = int(input("Снятие денег \n --> ведите сумму :"))
            if d > account.balance:
                print("Недостаточно средств на счёте")
            elif d <= 0:
                print("Сумма снятия должна быть положительной")
            else:
                account.withdraw(d)
                print(f"Баланс: {account.balance}", end="$\n")
                break
    elif x == '4':
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите снова.")
