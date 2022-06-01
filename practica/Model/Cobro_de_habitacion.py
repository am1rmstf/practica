#!/usr/bin/python
#-*- coding: utf-8 -*-
from datetime import datetime

from Model.Habitacion import Habitacion

class Cobro_de_habitacion:
    def __init__(self, fecha_de_pago, cliente, habitacion):
        self.__fecha_de_pago = fecha_de_pago
        self.__valor_total = 0.0
        self.ref_cliente = cliente
        self.ref_habitacion = habitacion
        self.habitaciones = []
        

    @property
    def fecha_de_pago(self):
        return self.__fecha_de_pago

    @fecha_de_pago.setter
    def fecha_consulta(self, valor):
        self.__fecha_de_pago = datetime.strptime(valor, '%d-%m-%Y')
    
    @property
    def valor_total(self):
        return self.__valor_total

    @valor_total.setter
    def valor_total(self, valor):
        self.__valor_total = valor
    
    def __str__(self):
        return str(self.ref_cliente) + ' - ' + str(self.ref_habitacion)
