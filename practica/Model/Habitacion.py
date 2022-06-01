#!/usr/bin/python
#-*- coding: utf-8 -*-

class Habitacion:
    def __init__(self, codigo, tipo):
        self.__codigo = codigo
        self.__tipo = tipo
    
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    def __str__(self):
        return self.__codigo + ' - ' + self.__valor   