class User:

    def __init__(self,nombre,correo):
        self.nombre = nombre
        self.correo = correo
        self.account_balance=0
    
    def situacion(self):
        return self.nombre, self.correo, self.account_balance

    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdrawal (self, amount) :
        self.account_balance -= amount
    
    # def display_user_balance (self, amount) :
    #     self.account_balance = amount

    # def display_situation(self):
    #     return self.nombre, self.correo, self.account_balance