class Producto:
    def __init__(self, id, nombreproducto, precio):
        self.id = id
        self.nombreproducto = nombreproducto
        self.precio = precio

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombreproducto(self):
        return self.nombreproducto

    def set_nombreproducto(self, nombreproducto):
        self.nombreproducto = nombreproducto

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio



    def guardar_datosproducto(producto):
        with open('productos.txt', 'a') as archivo:
            archivo.write(f"{producto.id},{producto.nombreproducto},{producto.precio} \n")




