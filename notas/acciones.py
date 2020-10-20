import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"ok, {usuario[1]} vamos  a crear una nota")

        titulo = input("Introduce el titulo de tu nota: \n")
        descripcion = input("Introduce el contenido de tu nota: \n")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\n Perfecto has guardado la nota: {nota.titulo} \n")

        else:
            print(f"\n No se ha guardado la nota {ususario[1]}")

    def mostrar(self, usuario):
        print(f"Estas son tus notas {usuario[1]}")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n*****************************")
            print(nota[2])
            print(nota[3])
            print("\n*****************************")

    def borrar(self, usuario):
        print(f"\n {usuario[1]} deseas borrar una nota")

        titulo = input("Introduce el titulo de la nota que deseas borrar:\n")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: \n {nota.titulo}")

        else:
            print("No se ha borrado correctamente la nota, intenta de nuevo")
        