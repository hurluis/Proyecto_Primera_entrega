    # Todas las prueba sunitarias importan la biblioteca unittest
import unittest
import crear_tablero_logica
# Las pruebas importan los modulos que hacen el trabajo

class DispararTest(unittest.TestCase):

    # test asegura que la colocación de barcos en el tablero con las coordenadas proporcionadas no cause excepciones inesperadas
    def test_ColocacionCorrectaBarcos(self):
        # Número de filas y columnas válidas
        filas = 5
        columnas = 7
        # Coordenadas válidas de los barcos
        barcos_preestablecidos = [(2, 3), (4, 5), (1, 1)]
        # Crear el tablero
        tablero = crear_tablero_logica.TableroBarcos(filas, columnas)
        # Colocar los barcos en el tablero
        try:
            tablero.colocar_barcos(barcos_preestablecidos)
            self.assertTrue(True)  # No debería lanzar ninguna excepción
        #si los barcos estan mas colocados se manda a la excepcion dispararse
        except (crear_tablero_logica.FilasColumasCeroError, crear_tablero_logica.BarcoFueraTableroError) as e:
            self.fail(f"Se lanzó una excepción inesperada: {e}")
      
    #test asegura que las filas y columnas ingresadas son las mismas que se muestran
    def test_CreacionTableroValido(self):
        # Número de filas y columnas válidas
        filas = 6
        columnas = 8
        #valida que sea la excepcion esperada
        try:
            tablero = crear_tablero_logica.TableroBarcos(filas, columnas)
            self.assertIsInstance(tablero, crear_tablero_logica.TableroBarcos)
            self.assertEqual(len(tablero.tablero), filas)
            self.assertEqual(len(tablero.tablero[0]), columnas)
        #sino pasa por aca se va a una de las excepciones
        except (crear_tablero_logica.FilasColumasCeroError, crear_tablero_logica.DatoStrError) as e:
            self.fail(f"Se lanzó una excepción inesperada: {e}")


    #test verifica que el tablero este vacio cuando no se entran barcos
    def test_TableroVacio(self):
        # Número de filas y columnas válidas
        filas = 4
        columnas = 5
        # Tablero sin barcos
        tablero = crear_tablero_logica.TableroBarcos(filas, columnas)
        # Verificar que el tablero está vacío
        self.assertEqual(tablero.tablero, [['O']*columnas for _ in range(filas)])


    #test asegura que se pueda crear bien un tablero de 1X1
    def test_Tablero1x1(self):
        # Número de filas y columnas válidas
        filas = 1
        columnas = 1
        # Coordenadas válidas de los barcos
        barcos_preestablecidos = [(1, 1)]
        # Crear el tablero
        tablero = crear_tablero_logica.TableroBarcos(filas, columnas)
          # Intentar colocar los barcos en el tablero
        try:
            tablero.colocar_barcos(barcos_preestablecidos)
            # Verificar que el tablero ahora tiene un barco en la posición (1, 1)
            self.assertEqual(tablero.tablero, [['X']])
            # También puedes verificar otras condiciones según tus requisitos
        except (crear_tablero_logica.FilasColumasCeroError, crear_tablero_logica.BarcoFueraTableroError) as e:
            self.fail(f"Se lanzó una excepción inesperada: {e}")


    #test valida que se puedan ingresar 10000 posiciones
    def test_10milX10mil(self):
        # Número de filas y columnas válidas
        filas = 10000
        columnas = 10000
        # Coordenadas válidas de los barcos
        barcos_preestablecidos = [(1, 1), (1, 2), (10000, 10000)]
        # Crear el tablero
        tablero = crear_tablero_logica.TableroBarcos(filas, columnas)
        # Colocar los barcos en el tablero
        try:
            tablero.colocar_barcos(barcos_preestablecidos)
            self.assertTrue(True)  # No debería lanzar ninguna excepción
        except (crear_tablero_logica.FilasColumasCeroError, crear_tablero_logica.BarcoFueraTableroError) as e:
            self.fail(f"Se lanzó una excepción inesperada: {e}")


    #test valida si que funcione la prueba asi todos los barcos esten en la misma fila
    def test_BarcosMismaFilaColumna(self):
        # Número de filas y columnas válidas
        filas = 3
        columnas = 4
        # Coordenadas válidas de los barcos
        barcos_preestablecidos = [(2, 1), (2, 2), (2, 3), (2, 4)]
        # Crear tablero
        tablero = crear_tablero_logica.TableroBarcos(filas, columnas)
        # Colocar los barcos en el tablero
        tablero.colocar_barcos(barcos_preestablecidos)
        # Verificar que el tablero se actualizó correctamente
        self.assertEqual(tablero.tablero, [['O', 'O', 'O', 'O'], ['X', 'X', 'X', 'X'], ['O', 'O', 'O', 'O']])


    #test valida si la variable no sea diferente de un entero
    def test_IngresoStr(self):
        # Crear el tablero
        filas = "dos"
        columnas = "tres"
        #lanzamiento de la excepcion
        with self.assertRaises(crear_tablero_logica.Exception):
            crear_tablero_logica.TableroBarcos(filas, columnas)


    #test controla el error donde los barcos estan fuera del limite
    def test_BarcoNoInLimite(self):
        # Crear el tablero
        filas = 5
        columnas = 5
        #crear tablero
        tablero = crear_tablero_logica.TableroBarcos(filas, columnas)
        barcos_preestablecidos = [(1, 1), (6, 7)]

        # Colocar los barcos en el tablero
        with self.assertRaises(crear_tablero_logica.BarcoFueraTableroError):
            tablero.colocar_barcos(barcos_preestablecidos)  


    #test controla el error si las filas en su valor se les ingresa 0
    def test_FilasSonCero(self):
        # Crear el tablero
        filas = 0
        columnas = 3
        # Utilizar la clase correcta
        tablero = crear_tablero_logica.TableroBarcos(filas, columnas)
        barcos_preestablecidos = [(4, 7), (2, 8), (8, 9)]

        # Colocar los barcos en el tablero
        with self.assertRaises(crear_tablero_logica.FilasColumasCeroError):
            tablero.colocar_barcos(barcos_preestablecidos)


    #test controla el error si las columnas en su valor se les ingresa 0
    def test_ColumnasSonCero(self):
        # Crear el tablero
        filas = 10
        columnas = 0
        # Utilizar la clase correcta
        tablero = crear_tablero_logica.TableroBarcos(filas, columnas)
        barcos_preestablecidos = [(4, 7), (2, 8), (8, 9)]

        # Colocar los barcos en el tablero
        with self.assertRaises(crear_tablero_logica.FilasColumasCeroError):
            tablero.colocar_barcos(barcos_preestablecidos)



if __name__ == '__main__':
    unittest.main()