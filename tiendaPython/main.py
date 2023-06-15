
from usuario import Usuario, guardar_datos
from producto import Producto
# Funciones 
def creaproductos():
    # Datos nuevo producto
    id = input("Ingrese id del producto: ")
    nombreproducto = input("Ingrese nombre del producto: ")
    precio = float(input("Ingrese precio del producto: "))
    # crear nuevo producto
    producto = Producto(id, nombreproducto, precio)
    producto.guardar_datosproducto()
    print("Producto creado")

def modificarproducto():
    # Producto que desea modificar
    nombreproducto = input("Ingrese nombre del producto que desea modificar: ")

    # Buscar
    productos = []
    with open('productos.txt', 'r') as archivo:
        for linea in archivo:
            id, nombreproducto, precio = linea.strip().split(',')
            productos.append(Producto(id, nombreproducto, float(precio)))

    producto_encontrado = False
    for producto in productos:
        if producto.get_nombreproducto() == nombreproducto:
            # Mostrar producto y modificar
            print(f"Producto encontrado: {producto.get_id()}, {producto.get_nombreproducto()}, {producto.get_precio()}")
            producto.set_id(input("Ingrese nueva id del producto: "))
            producto.set_nombreproducto(input("Ingrese nuevo nombre del producto: "))
            producto.set_precio(float(input("Ingrese nuevo precio del producto: ")))
            with open('productos.txt', 'w') as archivo:
                for producto in productos:
                    archivo.write(f"{producto.get_id()}, {producto.get_nombreproducto()}, {producto.get_precio()}\n")

            print("Producto modificado con éxito")
            producto_encontrado = True
            break

    if not producto_encontrado:
        print("Producto no encontrado")

def eliminarUsuario():
    # Leer usuarios del archivo
    usuarios = []
    with open('usuarios.txt', 'r') as archivo:
        for linea in archivo:
            nombre, apellido, nick, password = linea.strip().split(',')
            usuarios.append(Usuario(nombre, apellido, nick, password))

    # Mostrar los usuarios registrados (excepto "admi")
    print("Usuarios registrados:")
    for i, usuario in enumerate(usuarios):
        if usuario.get_nick() == "admi":
            continue  # Saltar el usuario "admi"
        print(f"{i+1}. {usuario.get_nombre()} {usuario.get_apellido()} ({usuario.get_nick()})")

    # Pedirnumero de usuario a eliminar
    num_eliminar = int(input("Ingrese el numero del usuario a eliminar: "))
    if num_eliminar < 1 or num_eliminar > len(usuarios) - 1:
        print("Numero de usuario invalido")
        return

    # Obtener el usuario a eliminar
    usuario_eliminar = usuarios[num_eliminar-1]
    nick_eliminar = usuario_eliminar.get_nick()

    # Confirmar la eliminación
    confirmar = input(f"Estas seguro de que deseas eliminar al usuario {nick_eliminar}? (s/n): ")
    if confirmar.lower() != "s":
        print("Eliminacion cancelada")
        return

    # Eliminar el usuario
    usuarios.remove(usuario_eliminar)
    print(f"El usuario {nick_eliminar} ha sido eliminado con exito")

    # Guardar los usuarios actualizados en el archivo
    with open('usuarios.txt', 'w') as archivo:
        for usuario in usuarios:
            archivo.write(f"{usuario.get_nombre()},{usuario.get_apellido()},{usuario.get_nick()},{usuario.get_password()}\n")

def facturacionTotal():
    # Leer todas las compras realizadas
    compras = []
    with open('factura.txt', 'r') as archivo:
        for linea in archivo:
            nick, nombreproducto, precio = linea.strip().split(',')
            compras.append((nick, nombreproducto, float(precio)))

    # factura total o por usuario
    opcion = input("¿Desea calcular la factura total (T) o por usuario (U)? ")
    opcion = opcion.lower()

    if opcion == "t":
        # Calcular la facturación total
        total = sum(precio for _, _, precio in compras)
        print(f"La factura total es: ${total:.2f}")
    elif opcion == "u":
        # usuarios con factura
        usuarios = set(nick for nick, _, _ in compras)
        print("Usuarios con factura:")
        for usuario in usuarios:
            print(usuario)

        # seleccion usuario para calcular la factura
        nick = input("Ingrese el nombre del usuario: ")
        while nick not in usuarios:
            print("Usuario inválido")
            nick = input("Ingrese el nombre del usuario: ")

        # Calcular la facturación total del usuario elegido
        total = sum(precio for n, _, precio in compras if n == nick)
        print(f"La factura total de {nick} es: ${total:.2f}")
    else:
        print("Opcion invalida")

    # otra factura
    opcion = input("¿Desea hacer otra factura? (S/N) ")
    opcion = opcion.lower()
    if opcion == "s":
        facturacionTotal()
    elif opcion == "n":
        print("Volviendo al menu principal...")
        
    else:
        print("Opcion invalida. Volviendo al menu principal...")

def verproductos(usuario):
    with open('productos.txt', 'r') as archivo:
        productos = []
        for linea in archivo:
            id, nombreproducto, precio = linea.strip().split(',')
            productos.append(Producto(id, nombreproducto, float(precio)))

    if productos:
        print("Productos disponibles:")
        for producto in productos:
            print(producto.get_id(), producto.get_nombreproducto(), producto.get_precio())
    else:
        print("No hay productos disponibles")

def Comprarproductos(usuario):
    productos = []
    productos_elegidos = []
    
    # productos disponibles
    with open('productos.txt', 'r') as archivo:
        for linea in archivo:
            id, nombreproducto, precio = linea.strip().split(',')
            productos.append(Producto(id, nombreproducto, float(precio)))

    # mostrar productos
    while True:
        print("Productos disponibles:")
        for i, producto in enumerate(productos):
            print(f"{i+1}. {producto.get_nombreproducto()} - ${producto.get_precio()}")

        # elijir  producto
        opcion = input("Elija un producto: ")
        if not opcion:
            break

        try:
            opcion = int(opcion)
            if opcion < 1 or opcion > len(productos):
                raise ValueError
        except ValueError:
            print("Opcion incorrecta")
            continue

        # Agregar producto
        producto_elegido = productos
        productos_elegidos.extend(producto_elegido)
        

        # agregar otro producto?
        opcion = input("¿Desea agregar otro producto? (s/n): ")
        if opcion.lower() == "n":
            break

    # Guardar factura
    with open('factura.txt', 'a') as archivo:
        for producto in productos_elegidos:
            archivo.write(f"{usuario.get_nombre()},{producto.get_nombreproducto()},{producto.get_precio()}\n")

def Modificarsusdatos(usuario):
    # buscar usuario
    usuarios = []
    usuario_encontrado = False
    with open('usuarios.txt', 'r') as archivo:
        for linea in archivo:
            nombre, apellido, nick, password = linea.strip().split(',')
            usuarios.append(Usuario(nombre, apellido, nick, password))
            if nick == usuario.get_nick():
                usuario_encontrado = True
                usuario_actual = Usuario(nombre, apellido, nick, password)
                break

    # datos actuales del usuario
    if usuario_encontrado:
        print("Sus datos actuales son:")
        print(f"Nombre: {usuario_actual.get_nombre()}")
        print(f"Apellidos: {usuario_actual.get_apellido()}")
        print(f"Nick: {usuario_actual.get_nick()}")
        print(f"Contraseña: {usuario_actual.get_password()}")

        # introducir nuevos datos
        nombre = input("Introduzca el nuevo nombre: ")
        if nombre:
            usuario_actual.set_nombre(nombre)

        apellidos = input("Introduzca los nuevos apellidos: ")
        if apellidos:
            usuario_actual.set_apellido(apellidos)

        nick = input("Introduzca el nuevo nick: ")
        if nick:
            nick_existe = False
            for u in usuarios:
                if u.get_nick() == nick:
                    nick_existe = True
                    break

            if nick_existe:
                print(f"{nick} ya esta siendo utilizado.")
            else:
                usuario_actual.set_nick(nick)

        password = input("Introduzca la nueva contraseña: ")
        if password:
            usuario_actual.set_password(password)

        # Actualizar
        with open('usuarios.txt', 'w') as archivo:
            for u in usuarios:
                if u.get_nick() == usuario_actual.get_nick():
                    archivo.write(f"{usuario_actual.get_nombre()},{usuario_actual.get_apellido()},{usuario_actual.get_nick()},{usuario_actual.get_password()}\n")
                else:
                    archivo.write(f"{u.get_nombre()},{u.get_apellido()},{u.get_nick()},{u.get_password()}\n")
        
        print("Sus datos han sido actualizados")
    else:
        print("Usuario no encontrado en usuarios.txt")

def inscribirse():
    nombre = input("Introduce tu nombre: ")
    apellido = input("Introduce tus apellido: ")
    nick = input("Introduce tu nick: ")
    password = input("Introduce tu contraseña: ")
    guardar_datos(nombre, apellido, nick, password)
    print("Usuario registrado correctamente")

def login():
    # Menu cliente
    menucliente = {
        "1": verproductos,
        "2": Comprarproductos,
        "3": Modificarsusdatos,
        "4": exit,
    }
    
    # Menu administrador
    menuadmi = {
        "1": creaproductos,
        "2": modificarproducto,
        "3": eliminarUsuario,
        "4": facturacionTotal,
        "5": exit,
    }
    with open('usuarios.txt', 'r') as archivo:
        admin_presente = False
        for linea in archivo:
            nombre, apellidos, usuario_archivo, password_archivo = linea.strip().split(',')
            if usuario_archivo == 'admi':
                admin_presente = True
                break
        if not admin_presente:
            with open('usuarios.txt', 'a') as archivo:
                archivo.write('Admin,Admin,admi,admi\n')
    usuario = None
    #Pedir datos de inicio
    while usuario is None:
        print("Iniciar sesion:")
        nick = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        with open('usuarios.txt', 'r') as archivo:
            for linea in archivo:
                nombre, apellidos, usuario_archivo, password_archivo = linea.strip().split(',')
                if usuario_archivo == nick and password_archivo == password:
                    print("Inicio de sesion correcto")
                    usuario = Usuario(nombre, apellidos, nick, password)
                    break
            else:
                print("Nombre de usuario o contraseña incorrectos")
                continue

    #Si usuario es admi mostrar menu admi
    if usuario.get_nick() == "admi" and usuario.get_password() == "admi":
        while True:
            print("Menu de administrador")
            print("Selecciona una opcion:")
            print("1. Crea Productos")
            print("2. Modificar producto")
            print("3. Eliminar usuario")
            print("4. facturacion total")
            print("5. Salir")
            opcion = input("> ")

            if opcion in menuadmi:
                menuadmi[opcion]()
                if opcion == "5":
                    break
            else:
                print("Opcion invalida. Intentalo de nuevo.")
    else:
        while True:
            print("Menu de cliente")
            print("Selecciona una opcion:")
            print("1. Ver Productos")
            print("2. Comprar Productos")
            print("3. Modificar datos personales")
            print("4. Salir")
            opcion = input("> ")

            if opcion in menucliente:
                menucliente[opcion](usuario)
                if opcion == "4":
                    break
            else:
                print("Opcion invalida. Intentalo de nuevo.")
    
    return usuario


def main():
    try:
        with open("usuarios.txt", "r"):
            pass
    except FileNotFoundError:
        with open("usuarios.txt", "w") as f:
            f.write("")

    try:
        with open("factura.txt", "r"):
            pass
    except FileNotFoundError:
        with open("factura.txt", "w") as f:
            f.write("")

    try:
        with open("productos.txt", "r"):
            pass
    except FileNotFoundError:
        with open("productos.txt", "w") as f:
            f.write("")

    ha_iniciado_sesion = False

    # Menu principal
    menu = {
        "1": inscribirse,
        "2": login,
        "3": exit,
    }

    while not ha_iniciado_sesion:
        print("Bienvenido")
        print("Selecciona una opcion:")
        print("1. Inscribirse")
        print("2. Hacer login")
        print("3. Salir")
        opcion = input("> ")

        if opcion in menu:
            if opcion == "1":
                inscribirse()
            elif opcion == "2":
                usuario = login()
                if usuario:
                    ha_iniciado_sesion = True
            elif opcion == "3":
                break
        else:
            print("Opcion invalida. Intentalo de nuevo.")

main()




