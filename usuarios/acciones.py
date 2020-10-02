# -*- coding: utf-8 -*-

import usuarios.usuario as modelo

class Acciones:

    def registro(self):
        print("Vamos a proceder a realizar tu registro!\n")
        nombre = input("Escribe tu nombre\n")
        apellidos = input("Escribe tu apellido \n")
        email = input("Escribe tu email \n")
        password = input("Escribe tu contraseña \n")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
    
        if registro[0] >= 1:
            print("perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente")
     
    def login(self):
        print("Por favor introduce tu clave y contraseña\n")
        email = input("Escribe tu email \n")
        password = input("Escribe tu contraseña \n")
    
    def error(self):
        print("Por favor solo introduce una de las 2 opciones indicadas")

    