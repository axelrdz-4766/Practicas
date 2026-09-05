class Account():
    def __init__(self, titular, money=0):
        self.titular = titular
        self._money = money

        if self.money < 0: raise ValueError("No puedes abrir una cuenta con negativos")

    @property
    def money(self):
        return self._money

    def deposit_money(self, cantidad):
        if cantidad <= 0: raise ValueError ("La cantidad ingresada debe de ser mayor a 0")

        self._money += cantidad

    def retirar_money(self, cantidad):
        if cantidad <= 0: raise ValueError("No se pueden cantidades negativas")

        if cantidad > self._money: raise ValueError("No puede retirar dinero que no tiene")

        self._money -= cantidad

    def show_account(self):
        return f'Titular: {self.titular}\nCantidad en la cuenta: ${self.money:.2f}'

account = Account("Axel", 100)

account.deposit_money(500)
account.retirar_money(250)

print(account.show_account())