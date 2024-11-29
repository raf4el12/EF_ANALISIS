Clase Cajero:
    Atributos:
        id_cajero: entero
        ubicacion: texto
        billetes: diccionario {denominacion: cantidad}

    Métodos:
        función actualizar_billetes(billetes: diccionario):
            Para cada denominacion, cantidad en billetes:
                Si denominacion en billetes:
                    billetes[denominacion] += cantidad
                Sino:
                    billetes[denominacion] = cantidad

        función obtener_billetes(monto: entero) -> diccionario:
            desglose = diccionario vacío
            Para cada denominacion, cantidad en billetes ordenado de mayor a menor:
                Si monto > 0:
                    cantidad_billetes = mínimo(monto // denominacion, cantidad)
                    Si cantidad_billetes > 0:
                        desglose[denominacion] = cantidad_billetes
                        monto -= cantidad_billetes * denominacion
            Si monto == 0:
                retornar desglose
            Sino:
                retornar None
