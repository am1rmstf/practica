from Cliente import *
from Cobro_de_habitacion import *
from Habitacion import *
from datetime import *

habitaciones = [
    Habitacion('Informal', 20),
    Habitacion('Familiar', 45),
    Habitacion('Vip', 70),
]

clientes = [
    Cliente('Pablo' , 'Banderas' , '095749985', 'PabloB@gmail.com'),
    Cliente('Juan'  , 'Contreras', '096672528', 'juanC@gmail.com'),
    Cliente('Dayana', 'Fernandez', '092767932', 'dayanaF@gmail.com'),
    Cliente('Maria' , 'Juana'    , '094798663', 'juanaM@gmail.com'),
 
]

reservaciones = [
   Cobro_de_habitacion('25-05-2022', clientes[0], habitaciones[2]),
   Cobro_de_habitacion('28-04-2022', clientes[1], habitaciones[3]),
   Cobro_de_habitacion('21-04-2022', clientes[2], habitaciones[2]),
   Cobro_de_habitacion('28-05-2022', clientes[3], habitaciones[2])
]

def reserva_x_cliente():
    for indice in range(0, len(reservaciones)):
        print('Recaudado por {} - {}.'.format(reservaciones[indice], reserva_x_cliente(indice)))


def menu_principal():
    print('Sistema de Reservas')

    opcion = 'N'
    while opcion == 'N':
        opcion = input('¿Desea Reservar una habitacion? [S-N]: ')
        if opcion == 'N':
            break

        nombre = input('Nombre del Cliente: ')
        apellido = input('Apellido del Cliente: ')
        cedula = input('Cedula del ciente ')
        correo = input('Correo del cliente: ')
        cliente = cliente(nombre, apellido, cedula, correo)
        
        menu_habitaciones()
        subopcion = int(input('Habitacion [1-2-3]: '))
        habitacion = None
        if (subopcion >=0 and subopcion <=3):
            especialidad = especialidad[subopcion-1]
        else:
            print('No ingresa de manera correcta la especialidad')
        
        fecha_reservacion = datetime.now()
        habitacion = Cobro_de_habitacion(fecha_reservacion, cliente, habitacion)
        habitaciones.append(habitacion)

        opcion = input('¿Desea salir? [S-N]')

    reserva_x_cliente

def menu_habitaciones():
    print('Seleccionar la habitacion: ')
    print('1 - Informal - $30')
    print('2 - Familiar - $35')
    print('3 - VIP - $50')


if __name__ == '__main__':
    menu_principal()