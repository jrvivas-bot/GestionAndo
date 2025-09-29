#Importo de datos.py el diccionario proyectos
from datos import proyectos

def agregar_proyecto(nombre):
    if nombre in proyectos:
        print(f"😱😱😱Error!!! Ya hay un proyecto con el nombre '{nombre}'🤦🏽")
        return False

    proyectos[nombre] = {
        "estado": "ACTIVO",
        "tareas": []
    }
    print(f"👌🏽 Proyecto '{nombre}' creado 👌🏽")
    return True


def modificar_proyecto(nombre_actual, nuevo_nombre=None, nuevo_estado=None):
    if nombre_actual not in proyectos:
        print("🤌🏽 Proyecto no encontrado 🤌🏽")
        return False

    proyecto = proyectos[nombre_actual]

    # Para cambiar el nombre
    if nuevo_nombre:
        if nuevo_nombre in proyectos:
            print(f"😱😱😱Error!!! Ya hay un proyecto con el nombre '{nuevo_nombre}'🤦🏽")
            return False
        # Esto mueve el contenido al nuevo nombre y borra el anterior
        proyectos[nuevo_nombre] = proyectos.pop(nombre_actual)
        proyecto = proyectos[nuevo_nombre]

    # Aca se cambia el estado
    if nuevo_estado and nuevo_estado.upper() in ["ACTIVO", "TERMINADO"]:
        proyecto["estado"] = nuevo_estado.upper()

    print(f"Proyecto '{nuevo_nombre or nombre_actual}' modificado.")
    return True

