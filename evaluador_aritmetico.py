class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, valor):
        self.elementos.append(valor)

    def pop(self):
        if len(self.elementos) > 0:
            return self.elementos.pop()
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

def evaluar_posfija(expresion):
    pila = Pila()
    tokens = expresion.split()
    
    for token in tokens:
        # Si es un número, lo metemos a la pila
        if token.isdigit():
            pila.push(int(token))
        else:
            # Si es un operador, sacamos los dos últimos números
            val2 = pila.pop()
            val1 = pila.pop()
            
            if token == '+':
                pila.push(val1 + val2)
            elif token == '-':
                pila.push(val1 - val2)
            elif token == '*':
                pila.push(val1 * val2)
            elif token == '/':
                pila.push(int(val1 / val2))
                
    return pila.pop()

# --- Bloque de prueba ---
if __name__ == "__main__":
    expresion = "3 4 + 2 *"  # Equivale a (3 + 4) * 2
    resultado = evaluar_posfija(expresion)
    print(f"Expresión posfija: {expresion}")
    print(f"Resultado de la evaluación: {resultado}")