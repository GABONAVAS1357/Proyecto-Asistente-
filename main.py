# -*- coding: utf-8 -*-

# INICIO DEL ASISTENTE

from usuarios import acciones

llamada = acciones.Acciones()

accion = input("Que deseas realizar?: \n 1- Registro \n 2- Login \n")

if accion == 1:
    llamada.registro()   

elif accion == 2:
    llamada.login()
    
else:
    llamada.error()
