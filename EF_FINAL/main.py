from cajero import Cajero
from cliente import Cliente
from cuenta import Cuenta
from utils import menu_principal

# Códigos de colores ANSI
ROJO = '\033[91m'
VERDE = '\033[92m'
AZUL = '\033[94m'
RESET = '\033[0m'

def imprimir_error(mensaje):
    print(f"{ROJO}{mensaje}{RESET}")

def imprimir_exito(mensaje):
    print(f"{VERDE}{mensaje}{RESET}")

def imprimir_info(mensaje):
    print(f"{AZUL}{mensaje}{RESET}")

def menu_principal():
    imprimir_info("\n--- Menú Principal ---")
    imprimir_info("1. Crear cliente")
    imprimir_info("2. Crear cuenta para un cliente")
    imprimir_info("3. Mostrar clientes y cuentas")
    imprimir_info("4. Realizar depósito")
    imprimir_info("5. Realizar retiro")
    imprimir_info("6. Consultar movimientos")
    imprimir_info("7. Realizar transferencia entre cuentas")
    imprimir_info("8. Salir")  # Agregar opción de transferencia
    opcion = input("Seleccione una opción: ")
    return opcion


def main():
    cajero = Cajero()  # Crear instancia del cajero

    while True:
        opcion = menu_principal()
        
        if opcion == "1":
            # Crear un nuevo cliente
            nombre = input("Ingrese el nombre del cliente: ")
            id_cliente = input("Ingrese un ID único para el cliente: ")
            
            if cajero.buscar_cliente(id_cliente):
                imprimir_error("Error: Ya existe un cliente con ese ID.")
            else:
                cliente = Cliente(nombre, id_cliente)
                cajero.agregar_cliente(cliente)
                imprimir_exito(f"Cliente {nombre} creado exitosamente.")
        
        elif opcion == "2":
            # Crear una cuenta para un cliente
            id_cliente = input("Ingrese el ID del cliente: ")
            cliente = cajero.buscar_cliente(id_cliente)
            
            if cliente:
                numero_cuenta = input("Ingrese el número de cuenta: ")
                saldo_inicial = float(input("Ingrese el saldo inicial: "))
                cuenta = Cuenta(numero_cuenta, saldo_inicial)
                cliente.agregar_cuenta(cuenta)
                imprimir_exito(f"Cuenta {numero_cuenta} creada con saldo inicial de {saldo_inicial}.")
            else:
                imprimir_error("Error: Cliente no encontrado.")
        
        elif opcion == "3":
            # Mostrar lista de clientes y sus cuentas
            imprimir_info("\n--- Clientes y sus Cuentas ---")
            if not cajero.clientes:
                imprimir_info("No hay clientes registrados.")
            else:
                for cliente in cajero.clientes:
                    print(cliente)
                    if not cliente.cuentas:
                        imprimir_info("  - No tiene cuentas asociadas.")
                    else:
                        for cuenta in cliente.cuentas:
                            imprimir_info(f"  - {cuenta}")
        
        elif opcion == "4":
            # Realizar depósito
            id_cliente = input("Ingrese el ID del cliente: ")
            cliente = cajero.buscar_cliente(id_cliente)
            
            if cliente:
                numero_cuenta = input("Ingrese el número de cuenta: ")
                cuenta = next((cuenta for cuenta in cliente.cuentas if cuenta.numero_cuenta == numero_cuenta), None)
                
                if cuenta:
                    monto = float(input("Ingrese el monto a depositar: "))
                    if monto <= 0:
                        imprimir_error("Error: El monto debe ser mayor a 0.")
                    else:
                        cuenta.depositar(monto)
                        cuenta.mostrar_movimientos()  # Mostrar los movimientos después del depósito
                else:
                    imprimir_error("Error: Cuenta no encontrada.")
            else:
                imprimir_error("Error: Cliente no encontrado.")
        
        elif opcion == "5":
            # Realizar retiro
            id_cliente = input("Ingrese el ID del cliente: ")
            cliente = cajero.buscar_cliente(id_cliente)
            
            if cliente:
                numero_cuenta = input("Ingrese el número de cuenta: ")
                cuenta = next((cuenta for cuenta in cliente.cuentas if cuenta.numero_cuenta == numero_cuenta), None)
                
                if cuenta:
                    monto = float(input("Ingrese el monto a retirar: "))
                    if monto > cuenta.saldo:
                        imprimir_error("Error: Fondos insuficientes.")
                    else:
                        cuenta.retirar(monto)
                        cuenta.mostrar_movimientos()  # Mostrar los movimientos después del retiro
                else:
                    imprimir_error("Error: Cuenta no encontrada.")
            else:
                imprimir_error("Error: Cliente no encontrado.")
        
        elif opcion == "6":
            # Consultar movimientos
            id_cliente = input("Ingrese el ID del cliente: ")
            cliente = cajero.buscar_cliente(id_cliente)
            
            if cliente:
                numero_cuenta = input("Ingrese el número de cuenta: ")
                cuenta = next((cuenta for cuenta in cliente.cuentas if cuenta.numero_cuenta == numero_cuenta), None)
                
                if cuenta:
                    cuenta.mostrar_movimientos()
                else:
                    imprimir_error("Error: Cuenta no encontrada.")
            else:
                imprimir_error("Error: Cliente no encontrado.")
        
        elif opcion == "7":
            # Realizar transferencia entre cuentas
            id_cliente_origen = input("Ingrese el ID del cliente (origen): ")
            cliente_origen = cajero.buscar_cliente(id_cliente_origen)
            
            if cliente_origen:
                numero_cuenta_origen = input("Ingrese el número de cuenta de origen: ")
                numero_cuenta_destino = input("Ingrese el número de cuenta destino: ")
                monto = float(input("Ingrese el monto a transferir: "))
                
                # Verificar si el monto es positivo
                if monto <= 0:
                    imprimir_error("Error: El monto debe ser mayor que 0.")
                    continue
                
                # Realizar la transferencia
                cliente_origen.realizar_transferencia(numero_cuenta_origen, numero_cuenta_destino, monto)
            else:
                imprimir_error("Error: Cliente origen no encontrado.")
        
        elif opcion == "8":
            # Salir del programa
            imprimir_info("¡Gracias por usar el sistema!")
            break


if __name__ == "__main__":
    main()
