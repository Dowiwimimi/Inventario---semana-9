from modelos.producto import Producto

class Inventario:
    # es la clase encargada de gestionar los productos del sistema

    def __init__(self):
    # aquí se guardan todos los productos
        self.productos = []

    def añadir_producto(self, producto):
      #primero verifico que el id no esté repetido
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: ya existe un producto con ese ID.")
                return

        self.productos.append(producto)
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        # se busca el producto por id y lo elimino
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado correctamente.")
                return

        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        # este permite actualizar cantidad, precio o ambos
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)

                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                print("Producto actualizado correctamente.")
                return

        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        #búsqueda por coincidencia parcial, de manera no exacta
        encontrados = [
            p for p in self.productos
            if nombre.lower() in p.get_nombre().lower()
        ]

        if encontrados:
            print("Resultados de la búsqueda:")
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        # muestra todo el inventario
        if not self.productos:
            print("El inventario está vacío.")
            return

        print("Inventario actual:")
        for p in self.productos:
            print(p)
