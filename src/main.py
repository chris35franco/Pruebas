from datetime import datetime

def calcular_edad(fecha_nacimiento):
    hoy = datetime.today()
    nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    edad = hoy.year - nacimiento.year
    # Verifica si el cumpleaños ya pasó en el año actual
    if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
        edad -= 1
    return edad
