import csv

class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas
    
    def imprimir_datos(self):
        print(' \nDatos del vehículo ', type(self).__name__)
        print('Inserte la marca :', self.marca)
        print('Inserte el modelo:', self.modelo)
        print('Inserte el número de ruedas:', self.num_ruedas)

    def __str__(self):
        return f'Datos de Vehículo {type(self).__name__}: \nMarca {self.marca}, Modelo {self.modelo}, {self.num_ruedas} ruedas'
    
    def crear_archivo():
        try:
            archivo = open('vehiculos.csv', 'x')
            archivo.close()
        except FileExistsError:
            print("El archivo vehiculos.csv existe o ha sido creado previamente")
        except Exception as error:
            print('Se ha generado un error no previsto', type(error).__name__) 


    def guardar_datos_csv(self, automoviles):
        try: 
            archivo = open('vehiculos.csv', "w")
            datos = [(automovil.__class__, automovil.__dict__) for automovil in automoviles ]
            archivo_csv = csv.writer(archivo)
            archivo_csv.writerows(datos)
            archivo.close()
        except Exception as error:
            print("Se produjo un error al guardar los datos en el archivo:", error)

    def leer_datos_csv(self):  
        vehiculos = []
        try:
            with open('vehiculos.csv', "r") as archivo:
                archivo_csv = csv.reader(archivo)
                for vehiculo in archivo_csv:
                    vehiculos.append(vehiculo)
                archivo.close()
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe.")
        except Exception as error:
            print(f"Se produjo un error al leer los datos del archivo: {error}")
        return vehiculos

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, num_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def imprimir_datos(self):
        super().imprimir_datos()
        print('Inserte la velocidad en km/h:', self.velocidad)
        print('Inserte el cilindraje en cc:', self.cilindrada)
       

    def __str__(self):
        return f'{ super().__str__()}, {self.velocidad} Km/h, {self.cilindrada} cc'

class Particular(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, num_puesto):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.num_puesto = num_puesto

    def imprimir_datos(self):
        super().imprimir_datos()
        print('Inserte números de puesto:', self.num_puesto)

    def __str__(self):
        return  f'{super().__str__()}, {self.num_puesto} puestos'

class Carga(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, peso):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.peso = peso

    def imprimir_datos(self):
        super().imprimir_datos()
        print('Inserte peso:', self.peso)

    def __str__(self):
        return f'{super().__str__()}, {self.peso} kg'

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, tipo):
        super().__init__(marca, modelo, num_ruedas)
        self.tipo = tipo

    def imprimir_datos(self):
        super().imprimir_datos()
        print('Inserte el tipo :', self.tipo)

    def __str__(self):
        return f'{ super().__str__()}, Tipo: {self.tipo}'

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, num_ruedas, tipo, num_radios, cuadro, motor):
        super().__init__(marca, modelo, num_ruedas, tipo)
        self.num_radios = num_radios
        self.cuadro = cuadro
        self.motor = motor

    def imprimir_datos(self):
        super().imprimir_datos()
        print('Inserte número de radios :', self.num_radios)
        print('Inserte cuadro :', self.cuadro)
        print('Inserte motor:', self.motor)


    def __str__(self):
        return f'{ super().__str__()}, Número de radios: {self.num_radios} , Cuadro: {self.cuadro}, Motor: {self.motor}'








