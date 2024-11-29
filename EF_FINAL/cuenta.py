class Cuenta:
    def __init__(self, numero_cuenta, saldo_inicial=0):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial
        self.movimientos = []  # Lista de movimientos de la cuenta

    def agregar_movimiento(self, tipo, monto):
        """
        Registra un movimiento en la cuenta.
        tipo: 'ingreso' o 'egreso'
        monto: cantidad del movimiento
        """
        if tipo not in ["ingreso", "egreso"]:
            raise ValueError("El tipo de movimiento debe ser 'ingreso' o 'egreso'.")
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que 0.")
        if tipo == "egreso" and monto > self.saldo:
            raise ValueError("Fondos insuficientes para realizar el egreso.")

        # Registrar movimiento y ajustar saldo
        self.movimientos.append({"tipo": tipo, "monto": monto, "saldo": self.saldo + monto if tipo == "ingreso" else self.saldo - monto})
        self.saldo += monto if tipo == "ingreso" else -monto

    def depositar(self, monto):
        """
        Realiza un depósito en la cuenta.
        """
        try:
            self.validar_monto(monto)
            self.agregar_movimiento("ingreso", monto)
            print(f"Depósito realizado exitosamente en la cuenta {self.numero_cuenta}. Saldo actual: {self.saldo:.2f}")
        except ValueError as e:
            print(f"Error al realizar el depósito: {e}")

    def retirar(self, monto):
        """
        Realiza un retiro de la cuenta.
        """
        try:
            self.validar_monto(monto)
            if monto <= self.saldo:
                self.agregar_movimiento("egreso", monto)
                print(f"Retiro realizado exitosamente. Saldo actual: {self.saldo:.2f}")
            else:
                print("Error: Fondos insuficientes.")
        except ValueError as e:
            print(f"Error al realizar el retiro: {e}")

    def transferir(self, monto, cuenta_destino):
        """
        Realiza una transferencia de saldo a otra cuenta.
        """
        try:
            if not isinstance(cuenta_destino, Cuenta):
                print("Error: La cuenta destino no es válida.")
                return

            self.validar_monto(monto)

            if monto <= self.saldo:
                self.agregar_movimiento("egreso", monto)
                cuenta_destino.agregar_movimiento("ingreso", monto)
                print(f"Transferencia realizada exitosamente. Saldo actual: {self.saldo:.2f}")
            else:
                print("Error: Fondos insuficientes para la transferencia.")
        except ValueError as e:
            print(f"Error al realizar la transferencia: {e}")

    def mostrar_movimientos(self):
        """
        Muestra todos los movimientos realizados en la cuenta.
        """
        if not self.movimientos:
            print("No hay movimientos registrados.")
        else:
            print("\n--- Movimientos de la cuenta ---")
            for idx, movimiento in enumerate(self.movimientos, start=1):
                tipo = "Depósito" if movimiento["tipo"] == "ingreso" else "Retiro"
                print(f"{idx}. {tipo}: {movimiento['monto']:.2f}, Saldo después del movimiento: {movimiento['saldo']:.2f}")

    def __str__(self):
        """
        Representación en cadena de la cuenta.
        """
        return f"Cuenta: {self.numero_cuenta}, Saldo: {self.saldo:.2f}, Movimientos: {len(self.movimientos)}"

    def validar_monto(self, monto):
        """
        Valida que el monto sea un número positivo.
        """
        if not isinstance(monto, (int, float)):
            raise ValueError("El monto debe ser un número.")
        if monto <= 0:
            raise ValueError("El monto debe ser positivo.")
