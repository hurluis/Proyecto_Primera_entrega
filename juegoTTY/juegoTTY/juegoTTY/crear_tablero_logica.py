#error si la fila o columna ingresada es cero
class FilasColumasCeroError(IndexError):
    pass

#error si el barco esta fuera de los limites 
class BarcoFueraTableroError(ValueError):
    pass

#error si el usuario entra un caracter diferente a un entero
class DatoStrError(Exception):
    pass
#se inicializan las clases con los tipos de errores que lanzaremos


class TableroBarcos:
    #metodo constructor de las variables que se implementaran en los metodos
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.validar_tipo_dato()  # Llama a la validación de tipo en la inicialización  
        self.tablero = self.crear_tablero()

    #metodo para validar que el dato ingresado por el usuario sea un entero
    def validar_tipo_dato(self):
        try:
            self.filas = int(self.filas)
            self.columnas = int(self.columnas)
        except ValueError:
            raise Exception("Error: No ingrese el valor como un texto, ponga números enteros")


    #metodo para crear el tablero de juego
    def crear_tablero(self):
        return [['O' for _ in range(self.columnas)] for _ in range(self.filas)]

    #metodo que controla el error que el tablero no sea de tamaño 0X0
    def validar_tamaño(self):
        if self.filas <= 0:
            raise FilasColumasCeroError("Error: No puede crear un tablero con filas  iguales o menores a cero.")
        if self.columnas <= 0:
            raise FilasColumasCeroError("Error: No puede crear un tablero con columnas iguales o menores a cero.")

    #metodo que imprime el tablero    
    def mostrar_tablero(self):
        for fila in self.tablero:
            print(' '.join(fila))

    #metodo para colocar el barco en el tablero y también controla el error del barco si esta dentro del tablero
    def colocar_barcos(self, barcos):
        self.validar_tamaño()

        for barco in barcos:
            fila, columna = barco

            if 0 <= fila < self.filas and 0 <= columna < self.columnas:
                self.tablero[fila][columna] = 'X'
                print(f"Intentando colocar barco en fila {fila+1}, columna {columna+1}")
            else:
                raise BarcoFueraTableroError("Error: El barco no está dentro de la dimensión esperada. Por favor, coloque elementos dentro de la fila y columna.")