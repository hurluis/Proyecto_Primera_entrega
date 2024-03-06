#importar los demas modulos
import juegoTTY_error

try:
    pass

except juegoTTY_error.CoordenadasFueraRangoError as err:
    print(str(err))

except juegoTTY_error.CoordenadasNegativas as err:
    print(str(err))

except juegoTTY_error.CoordenadasValorIncorrecto as err: 
    print(str(err))

except juegoTTY_error.ErrorMasDeDosCoordenadas as err:
    print(str(err))
