# -*- coding: utf-8 -*-

import usuarios.usuario as modelo
import notas.acciones

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
            print(f"\n perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\n No te has registrado correctamente")
     # revisar el error desde aca 18/10/2020 ultima calase vista 117
    def login(self):
        print("Por favor introduce tu clave y contraseña\n")

        try:
            email = input("Escribe tu email \n")
            password = input("Escribe tu contraseña \n")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\n Bienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
          #  print(type(e))
           # print(type(e).__name__)
            print(f"Login incorrecto, intenta de nuevo")
        
    def proximasAcciones(self, usuario):
        # print("""
        #acciones disponibles:
        #- Crear nota (crear)
        #- Mostrar tus notas (mostrar)
        #- Eliminar notas (eliminar)
        #- salir (salir)
        #""")
        
        accion = input("Que quieres hacer?. Elige una opcion:\n 1- Crear nota \n 2- Mostrar tus notas \n 3- Eliminar notas \n 4- salir \n")
        hazEl = notas.acciones.Acciones()

        if accion == "1":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "2":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "3":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "4":
            exit()
            print(f"Hasta luego {login[1]}")
            

        return None
    
    def error(self):
        print("Por favor solo introduce una de las 2 opciones indicadas")
        
        

    