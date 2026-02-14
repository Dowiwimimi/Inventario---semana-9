from servicios.inventario import Inventario
from modelos.producto import Producto


def mostrar_menu():
    print("\n Bienvenidos al sistema de gestión de inventarios \n")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Salir")


def cargar_productos_iniciales(inventario):
    # agrego algunos productos, sin embargo el usuario puede añadir más desde el menú

    p1 = Producto(1, "Figura coleccionable Hirono", 5, 18.50)
    p2 = Producto(2, "Labial matte", 12, 4.25)
    p3 = Producto(3, "Bolso casual", 7, 22.00)

    inventario.añadir_producto(p1)
    inventario.añadir_producto(p2)
    inventario.añadir_producto(p3)


def main():
    inventario = Inventario()

    # se carga los productos de prueba
    cargar_productos_iniciales(inventario)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = int(input("Ingrese ID: "))
                nombre = input("Ingrese nombre: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))

                nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(nuevo_producto)

            except ValueError:
                print("Entrada inválida. Por favor verifique los datos.")

        elif opcion == "2":
            try:
                id_producto = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("ID inválido.")

        elif opcion == "3":
            try:
                id_producto = int(input("Por favor ingrese el ID del producto a actualizar: "))

                cantidad = input("Nueva cantidad (deje vacío si no desea cambiar): ")
                precio = input("Nuevo precio (deje vacío si no desea cambiar): ")

                nueva_cantidad = int(cantidad) if cantidad else None
                nuevo_precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

            except ValueError:
                print("Datos inválidos.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
