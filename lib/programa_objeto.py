class Cliente:
    def __init__(self,nombre,direc,tel,dni=" "):
        self.nombre= nombre
        self.direc= direc
        self.tel= tel
        self.DNI= dni
    def info(self):
        print("Nombre: ",self.nombre)
        print("Direccion: ",self.direc)
        print("Telefono: ",self.tel)
        print("DNI: ",self.dni)
class Clientes:
    def __init__(self):
        self.clientes=[]
        pass
    def add(self,nombre,direc,tel,dni):
        client=Cliente(nombre,direc,tel,dni)
        self.clientes.append(client)
    def list(self):
        for c in self.clientes:
            print(c.nombre)
    def sort(self):
        self.clientes.sort(key=lambda objeto: objeto.nombre)
clientes=Clientes()
clientes.add("Juan Perez","25 de Mayo 334","223444322","46876927")
clientes.add("Jose Diaz","24 de Julio 964","293474122","21864526")
clientes.list()
clientes.sort()
