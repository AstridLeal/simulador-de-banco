# Programa principal para controlar un Banco compuesto por Cuentas
from Bank import Banco, AbortTransaction

# Crear una instancia del Banco
objeto_Banco = Banco('9 a 5', '123 Calle Principal, Ciudad, País', '(650) 555-1212')

# Código principal
while True:
    print()
    print('Para obtener el saldo de una cuenta, presione b')
    print('Para cerrar una cuenta, presione c')
    print('Para hacer un depósito, presione d')
    print('Para obtener información del banco, presione i')
    print('Para abrir una nueva cuenta, presione o')
    print('Para salir, presione q')
    print('Para mostrar todas las cuentas, presione s')
    print('Para hacer un retiro, presione w')
    print()
    action = input('¿Qué desea hacer? ')
    action = action.lower()
    print()
    
    try:
      if action == 'b':
        objeto_Banco.saldo()
      elif action == 'c':
        objeto_Banco.cerrarCuenta()
      elif action == 'd':
        objeto_Banco.depositar()
      elif action == 'i':
        objeto_Banco.obtenerInformacion()
      elif action == 'o':
        objeto_Banco.abrirCuenta()
      elif action == 'q':
        break
      elif action == 's':
        objeto_Banco.mostrar()
      elif action == 'w':
        objeto_Banco.retirar()
    except AbortTransaction as error:
        # Imprimir el texto del mensaje de error
        print(error)
      
print('Hecho')