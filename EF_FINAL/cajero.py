class Cajero:
    def __init__(self):
        """
        Constructor para inicializar el cajero.
        """
        self.clientes = []  # Lista de clientes
        # Inventario de billetes: denominación -> cantidad
        self.inventario_billetes = {200: 50, 100: 100, 50: 200, 20: 500}

    def agregar_cliente(self, cliente):
        """
        Agrega un cliente al sistema si no está registrado.
        """
        if self.buscar_cliente(cliente.id_cliente) is None:
            self.clientes.append(cliente)
            print(f"Cliente {cliente.nombre} registrado exitosamente.")
        else:
            print(f"Error: El cliente con ID {cliente.id_cliente} ya está registrado.")

    def buscar_cliente(self, id_cliente):
        """
        Busca un cliente en el sistema por su ID.
        """
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None

    def mostrar_clientes(self):
        """
        Muestra todos los clientes registrados.
        """
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            self.clientes.sort(key=lambda cliente: cliente.obtener_saldo_total(), reverse=True)
            for cliente in self.clientes:
                print(cliente)

    def ordenar_billetes(self):
        """
        Ordena las denominaciones de billetes de mayor a menor utilizando Quicksort.
        """
        denominaciones = list(self.inventario_billetes.keys())
        
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x > pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x < pivot]
            return quicksort(left) + middle + quicksort(right)
        
        return quicksort(denominaciones)

    def calcular_retiro(self, monto):
        """
        Calcula la combinación óptima de billetes para un retiro usando un algoritmo voraz.
        """
        denominaciones = self.ordenar_billetes()  # Aseguramos que están ordenadas de mayor a menor
        billetes_usados = {}
        for denom in denominaciones:
            if monto == 0:
                break
            cantidad_disponible = self.inventario_billetes[denom]
            billetes_necesarios = min(monto // denom, cantidad_disponible)
            if billetes_necesarios > 0:
                billetes_usados[denom] = billetes_necesarios
                monto -= denom * billetes_necesarios

        if monto > 0:
            print("No se puede completar el retiro con el inventario actual.")
            return None
        else:
            # Actualizar inventario de billetes
            for denom, cantidad in billetes_usados.items():
                self.inventario_billetes[denom] -= cantidad
            return billetes_usados

    def mostrar_inventario(self):
        """
        Muestra el inventario actual de billetes.
        """
        print("\n--- Inventario de Billetes ---")
        for denom, cantidad in sorted(self.inventario_billetes.items(), reverse=True):
            print(f"Denominación: {denom}, Cantidad: {cantidad}")

    def buscar_denominacion(self, denominacion):
        """
        Busca una denominación en el inventario utilizando búsqueda binaria.
        """
        denominaciones = self.ordenar_billetes()  # Aseguramos que están ordenadas
        izquierda, derecha = 0, len(denominaciones) - 1

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if denominaciones[medio] == denominacion:
                return True
            elif denominaciones[medio] < denominacion:
                derecha = medio - 1
            else:
                izquierda = medio + 1

        return False

    def registrar_movimiento(self, cuenta, tipo, monto):
        """
        Registra un movimiento en una cuenta y actualiza el saldo.
        """
        cuenta.registrar_movimiento(tipo, monto)

    def realizar_deposito(self, id_cliente, numero_cuenta, monto):
        """
        Realiza un depósito en una cuenta de un cliente.
        """
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            cuenta = cliente.buscar_cuenta(numero_cuenta)
            if cuenta:
                cuenta.depositar(monto)
                print(f"Depósito de {monto} realizado exitosamente.")
            else:
                print(f"Error: La cuenta {numero_cuenta} no existe.")
        else:
            print(f"Error: El cliente con ID {id_cliente} no está registrado.")

    def realizar_retiro(self, id_cliente, numero_cuenta, monto):
        """
        Realiza un retiro de una cuenta de un cliente, considerando el inventario de billetes.
        """
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            cuenta = cliente.buscar_cuenta(numero_cuenta)
            if cuenta:
                if monto <= cuenta.saldo:
                    billetes_usados = self.calcular_retiro(monto)
                    if billetes_usados:
                        cuenta.retirar(monto)
                        print(f"Retiro de {monto} realizado exitosamente.")
                    else:
                        print("Error: No se pudo realizar el retiro debido a la falta de billetes.")
                else:
                    print("Error: Fondos insuficientes en la cuenta.")
            else:
                print(f"Error: La cuenta {numero_cuenta} no existe.")
        else:
            print(f"Error: El cliente con ID {id_cliente} no está registrado.")

    def realizar_transferencia(self, id_cliente, numero_cuenta_origen, numero_cuenta_destino, monto):
        """
        Realiza una transferencia entre dos cuentas de un cliente.
        """
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            cuenta_origen = cliente.buscar_cuenta(numero_cuenta_origen)
            cuenta_destino = cliente.buscar_cuenta(numero_cuenta_destino)
            if cuenta_origen and cuenta_destino:
                cuenta_origen.transferir(monto, cuenta_destino)
                print(f"Transferencia de {monto} realizada exitosamente.")
            else:
                print("Error: Una de las cuentas no existe.")
        else:
            print(f"Error: El cliente con ID {id_cliente} no está registrado.")
