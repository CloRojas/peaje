from vehiculos import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta
import csv

automovil1 = Automovil('Toyota', 'Yaris', 4, 120, 800)
automovil2 = Automovil('Fiat', 'Palio', 4, 95, 1200)
automovil3 = Automovil('Ford', 'Fiesta', 4, 125, 1500)


autoparticular1 = Particular("Ford", "Fiesta", 4, 180, 500, 5)
autocarga1 = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
bicicleta1 = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta1 = Motocicleta("BMW", "F800s",2,"Deportiva",21,"Doble Viga", "2T")



# print('Cuantos vehiculos desea insertar:')
# print('')

# automovil1.imprimir_datos()
# automovil2.imprimir_datos()
# automovil3.imprimir_datos()
# autoparticular1.imprimir_datos()
# autocarga1.imprimir_datos()
# bicicleta1.imprimir_datos()
# motocicleta1.imprimir_datos()





print('\nImprimiendo por pantalla los Vehículos:\n')
print(automovil1)
print(automovil2)
print(automovil3)
print(autoparticular1)
print(autocarga1)
print(bicicleta1)
print(motocicleta1)


print('\nMotocicleta es instancia con relación a Vehículo:', isinstance(motocicleta1, Vehiculo))
print('Motocicleta es instancia con relación a Automovil:', isinstance(motocicleta1, Automovil))
print('Motocicleta es instancia con relación a Automóvil Particular:', isinstance(motocicleta1, Particular))
print('Motocicleta es instancia con relación a Automóvil Carga:', isinstance(motocicleta1, Carga))
print('Motocicleta es instancia con relación a Bicicleta:', isinstance(motocicleta1, Bicicleta))
print('Motocicleta es instancia con relación a Motocicleta:', isinstance(motocicleta1, Motocicleta))

Vehiculo.crear_archivo()
automoviles = [automovil1, automovil2, automovil3, autoparticular1, autocarga1, bicicleta1, motocicleta1]

Vehiculo.guardar_datos_csv("vehiculos.csv", automoviles)


automoviles = Vehiculo.leer_datos_csv('vehiculos.csv')


if automoviles is not None:
    clases_impresas = set()
    for automovil in automoviles:
        nombre_clase_completo = automovil[0].split("'")[1]
        if nombre_clase_completo not in clases_impresas:
            nombre_clase = nombre_clase_completo.split('.')[-1]
            print("Lista de Vehículos", nombre_clase)
            clases_impresas.add(nombre_clase_completo)
        datos_vehiculo = automovil[1:]
        if datos_vehiculo:
            datos_vehiculo = ', '.join(datos_vehiculo)
            print(datos_vehiculo)
            print()
else:
    print("No se pudo recuperar la lista de vehículos.")

