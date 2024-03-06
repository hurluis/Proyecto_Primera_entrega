#importar 
import juegoTTY_error

#definir la clase principal para disparar

class Disparar:

    #metodo inicializador de la clase disparo
    def __init__(self, x,y, tablero=[[]]):
        self.coordenadaX=x
        self.coordenadaY=y
        self.ultimoDisparoX=0
        self.ultimoDisparoY=0
        self.tablero=tablero

    #metodo que recibe las coordenadas del objetivo y dispara
    def shoot(self):
        self.ultimoDisparoX=self.coordenadaX
        self.ultimoDisparoY=self.coordenadaY


        if isinstance(self.coordenadaX,float):
            self.coordenadaX= int(self.coordenadaX)
            print(self.coordenadaX)
        if isinstance(self.coordenadaY,float):
            self.coordenadaY = int(self.coordenadaY)
            print(self.coordenadaY)

        if not isinstance(self.coordenadaX,int) or not isinstance(self.coordenadaY,int):
            raise juegoTTY_error.CoordenadasValorIncorrecto
        if self.coordenadaX < 0 or self.coordenadaY<0:
            raise juegoTTY_error.CoordenadasNegativas()
        if self.coordenadaX >= len(self.tablero) or self.coordenadaY >= len(self.tablero[self.coordenadaX]):
            raise juegoTTY_error.CoordenadasFueraRangoError
        
        #error adicional
        if self.coordenadaX:
            pass

        #espacio para hacer otro error adicional

        if self.ultimoDisparoX==self.coordenadaX and self.ultimoDisparoY==self.coordenadaY:
            return False #true
        else:
            return False
        
        

#metodo que recibe las coordenadas del objetivo y devuelve si se ha impactado o no
    def check_impact(self):
        return False

#metodo que revisa si quedan barcos en el tablero y devuelve si el juego ha terminado o no
    def game_over(self):
        return False
    


    