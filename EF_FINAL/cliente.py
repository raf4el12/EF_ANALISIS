class Cliente:
    def __init__(self, nombre, id_cliente):
        """
        Constructor para inicializar un cliente.
        """
        self.nombre = nombre
        self.id_cliente = id_cliente
        self.cuentas = []  # Lista de cuentas asociadas al cliente

    def agregar_cuenta(self, cuenta):
        """
        Agrega una cuenta a la lista de cuentas del cliente.
        Verifica que la cuenta no esté duplicada.
        """
        if not self.buscar_cuenta(cuenta.numero_cuenta):
            self.cuentas.append(cuenta)
            print(f"Cuenta {cuenta.numero_cuenta} agregada exitosamente.")
        else:
            print(f"Error: La cuenta {cuenta.numero_cuenta} ya está asociada a este cliente.")

    def buscar_cuenta(self, numero_cuenta):
        """
        Busca y devuelve una cuenta asociada al cliente por su número.
        """
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                return cuenta
        return None

    def listar_cuentas(self):
        """
        Retorna una representación en cadena de todas las cuentas asociadas al cliente, ordenadas de mayor a menor saldo.
        """
        if not self.cuentas:
            return "No tiene cuentas asociadas."
        
        # Ordenar las cuentas de mayor a menor saldo
        cuentas_ordenadas = sorted(self.cuentas, key=lambda cuenta: cuenta.saldo, reverse=True)
        
        # Crear una representación en cadena para las cuentas ordenadas
        cuentas_str = "Cuentas de " + self.nombre + " (ordenadas por saldo):\n"
        cuentas_str += "\n".join([f"Cuenta {cuenta.numero_cuenta}: Saldo ${cuenta.saldo:,.2f}" for cuenta in cuentas_ordenadas])
        return cuentas_str

    def realizar_transferencia(self, numero_cuenta_origen, numero_cuenta_destino, monto):
        """
        Realiza una transferencia entre dos cuentas asociadas al cliente.
        """
        cuenta_origen = self.buscar_cuenta(numero_cuenta_origen)
        cuenta_destino = self.buscar_cuenta(numero_cuenta_destino)

        if cuenta_origen and cuenta_destino:
            cuenta_origen.transferir(monto, cuenta_destino)
        else:
            print("Error: Una de las cuentas no existe o no pertenece a este cliente.")

    def obtener_saldo_total(self):
        """
        Obtiene el saldo total de todas las cuentas asociadas al cliente.
        """
        total_saldo = sum([cuenta.saldo for cuenta in self.cuentas])
        return total_saldo

    def __str__(self):
        """
        Representación en cadena del cliente y sus cuentas.
        """
        return f"Cliente: {self.nombre} (ID: {self.id_cliente})\nCuentas:\n{self.listar_cuentas()}\nSaldo total: {self.obtener_saldo_total():.2f}"
