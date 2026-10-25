class Pila:
    def __init__(self, capacidad=8):
        self.capacidad = capacidad
        self.elementos = []
        self.tope = 0  # TOPE = 0 indica pila vacía

    def insertar(self, valor):
        # Verificar desbordamiento (Overflow)
        if self.tope >= self.capacidad:
            print(f"¡Error! Desbordamiento (Overflow) al intentar insertar '{valor}'. Pila llena.")
            return False
        
        self.elementos.append(valor)
        self.tope += 1
        print(f"Insertar({valor}) -> Pila: {self.elementos} | TOPE = {self.tope}")
        return True

    def eliminar(self):
        # Verificar subdesbordamiento (Underflow)
        if self.tope == 0:
            print("¡Error! Subdesbordamiento (Underflow): La pila está vacía.")
            return None
        
        valor = self.elementos.pop()
        self.tope -= 1
        print(f"Eliminar() -> Extraído: {valor} | Pila: {self.elementos} | TOPE = {self.tope}")
        return valor

# --- Bloque principal de ejecución ---
if __name__ == "__main__":
    print("--- INICIO DE LA SIMULACIÓN DE LA PILA ---")
    mi_pila = Pila(capacidad=8)

    mi_pila.insertar('X')  # a
    mi_pila.insertar('Y')  # b
    mi_pila.eliminar()     # c (Z)
    mi_pila.eliminar()     # d (T)
    mi_pila.eliminar()     # e (U) -> Generará subdesbordamiento
    mi_pila.insertar('V')  # f
    mi_pila.insertar('W')  # g
    mi_pila.eliminar()     # h (p)
    mi_pila.insertar('R')  # i

    print("\n--- ESTADO FINAL ---")
    print(f"Elementos finales en la pila: {mi_pila.elementos}")
    print(f"Cantidad de elementos: {mi_pila.tope}")
    print(f"Valor del puntero TOPE: {mi_pila.tope}")