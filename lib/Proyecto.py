class Proyecto:
	def __init__(self, nombre,estado="ACTIVO"):
        self.nombre=nombre
        self.estado=estado
        self.tareas=[]
        
	def add_tarea(self, nombre,descripcion,estado="ACTIVO"):
        tarea={"nombre":nombre,"estado":estado}
        self.tareas.append(tarea)
        
    def list(self):
        