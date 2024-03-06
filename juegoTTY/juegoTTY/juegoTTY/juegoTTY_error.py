class CoordenadasFueraRangoError(IndexError):
    def __str__(self):
        return "Error: Las coordenadas ingresadas para el disparo estan fuera del rango del tablero de juego. "
    
class CoordenadasValorIncorrecto(ValueError):
    def __str__(self):
        return "Error: Las coordenadas ingresadas no son de tipo entero (int) y deben serlo"

class CoordenadasNegativas(Exception):
    def __str__(self):
        return "Error: Las coordenadas ingresadas fueron negativas y deben ser positivas"

class ErrorMasDeDosCoordenadas(Exception):
    def __str__(self):
        return "Error: Las coordenadas ingresadas fueron mas de dos y pueden ser solo de a un numero entero por ingreso de dato"
    