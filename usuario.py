class Usuario:
    def __init__(self, nombre, apellido, nick, password):
        self.nombre = nombre
        self.apellido = apellido
        self.nick = nick
        self.password = password

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_nick(self):
        return self.nick

    def set_nick(self, nick):
        self.nick = nick

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password


def guardar_datos(nombre, apellidos, nick, password):
    with open('usuarios.txt', 'a') as archivo:
        archivo.write(f"{nombre},{apellidos},{nick},{password}\n")



