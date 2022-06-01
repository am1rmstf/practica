#!/usr/bin/python
#-*- coding: utf-8 -*-

class Cliente:
    def __init__(self, nombre, apellido, cedula, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__correo = correo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, valor):
        self.__apellido = valor

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, valor):
        self.__cedula = valor  

    @property
    def correo(self):
        return self.__correo

    @apellido.setter
    def correo(self, valor):
        self.__correo = valor  
    
    def __str__(self):
        return self.__nombre + ' ' + self.__apellido + ' ' + self.__cedula + ' ' + self.__correo
    

