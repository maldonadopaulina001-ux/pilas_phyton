class PilaTorre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def push(self, disco):
        self.elementos.append(disco)

    def pop(self):
        if len(self.elementos) > 0:
            return self.elementos.pop()
        return None

def resolver_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        disco = origen.pop()
        destino.push(disco)
        print(f"Mover disco {disco} desde la torre '{origen.nombre}' hacia la torre '{destino.nombre}'")
        return
    
    resolver_hanoi(n - 1, origen, auxiliar, destino)
    
    disco = origen.pop()
    destino.push(disco)
    print(f"Mover disco {disco} desde la torre '{origen.nombre}' hacia la torre '{destino.nombre}'")
    
    resolver_hanoi(n - 1, auxiliar, destino, origen)

# --- Bloque de prueba ---
if __name__ == "__main__":
    # Creamos las tres torres como Pilas
    torre_origen = PilaTorre("Origen")
    torre_auxiliar = PilaTorre("Auxiliar")
    torre_destino = PilaTorre("Destino")

    # Inicializamos con 3 discos (el disco 3 es el más grande en la base, el 1 el más pequeño arriba)
    num_discos = 3
    for d in range(num_discos, 0, -1):
        torre_origen.push(d)

    print(f"--- INICIO DE TORRES DE HANOI ({num_discos} discos) ---")
    resolver_hanoi(num_discos, torre_origen, torre_destino, torre_auxiliar)
    print
          # --- Bloque principal de ejecución ---
if __name__ == "__main__":
    torre_origen = PilaTorre("Origen")
    torre_auxiliar = PilaTorre("Auxiliar")
    torre_destino = PilaTorre("Destino")

    num_discos = 3
    for d in range(num_discos, 0, -1):
        torre_origen.push(d)

    print(f"--- INICIO DE TORRES DE HANOI ({num_discos} discos) ---")
    resolver_hanoi(num_discos, torre_origen, torre_destino, torre_auxiliar)
    print("--- ¡RESOLUCIÓN COMPLETADA! ---")