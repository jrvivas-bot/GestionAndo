class Tarea:
    def __init__(self, nombre, descripcion, estado="Activo"):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Descripción:", self.descripcion)
        print("Estado:", self.estado)

    def cambiar_estado(self):
        if self.estado == "Activo":
            self.estado = "Finalizado"
        else:
            self.estado = "Activo"
