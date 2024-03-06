from crear_tablero_logica import*

#por ser un bloque de codigo suceptible a error poner lo que uqeremso que se ejecute en un try, 
#para que si no se da bien lo que esta planeado dirija al usuario al bloque de excepciones.
try:
    # Solicitar al usuario los valores de entrada

    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    tablero_barcos = TableroBarcos(filas, columnas)

    num_barcos = int(input("Ingrese el número de barcos: "))
    barcos = []
    
     # realizar el proceso
    for _ in range(num_barcos):
        try:
            fila = int(input("Ingrese la fila del barco: ")) - 1
            columna = int(input("Ingrese la columna del barco: ")) - 1
        except ValueError:
            raise Exception("Error: Ingrese valores válidos como números enteros.")
        
        barcos.append((fila, columna))
    
    # salidas
    tablero_barcos.colocar_barcos(barcos)

    print("\nTablero con barcos:")
    tablero_barcos.mostrar_tablero()

# casos de error

except FilasColumasCeroError as fcce:
    print(f"Error: {fcce}")
except BarcoFueraTableroError as bfte:
    print(f"Error: {bfte}")
except Exception as dse:
    print(f"Error inesperado: {dse}")