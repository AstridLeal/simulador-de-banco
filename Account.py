# Clase Cuenta
# Errores indicados por declaraciones "raise"
# Definir una excepción personalizada
class AbortTransaction(Exception): 
  '''lanzar esta excepción para abortar una transacción bancaria'''
  pass

class Cuenta():
  # Constructor de la clase Account
  def __init__(self, name, balance, password):
    self.name = name
    self.balance = int(balance)
    self.password = password

  def validateAmount(self, monto):
    try:
      monto = int(monto)
    except ValueError:
      raise AbortTransaction('El monto debe ser un número entero')
    if monto <= 0:
      raise AbortTransaction('El monto debe ser positivo')
    return monto
  

  def checkPasswordMatch(self, contraseña):
    if contraseña != self.contraseña:
      raise AbortTransaction('Contraseña incorrecta para esta cuenta')

  # Método para depositar en la cuenta
  def deposit(self, amountToDeposit, password):
    amountToDeposit = self.validateAmount(amountToDeposit)
    self.balance = self.balance + amountToDeposit
    return self.balance

  # Método para retirar dinero de la cuenta
  def withdraw(self, amountToWithdraw, password):
    amountToWithdraw = self.validateAmount(amountToWithdraw)
    if amountToWithdraw > self.balance:
      raise AbortTransaction('No puedes retirar más de lo que tienes en tu cuenta')
    self.balance = self.balance - amountToWithdraw
    return self.balance

  # Método para obtener el saldo de la cuenta
  def getBalance(self):
    return self.balance

  # Agregado para depuración
  def show(self):
    print(' Nombre:', self.name)
    print(' Saldo:', self.balance)
    print(' Contraseña:', self.password)
    print()