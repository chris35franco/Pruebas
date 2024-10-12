# main.py

class Reserva:
    def __init__(self, usuario, fecha, hora, numero_personas):
        self.usuario = usuario
        self.fecha = fecha
        self.hora = hora
        self.numero_personas = numero_personas

class SistemaReservas:
    def __init__(self):
        self.reservas = []

    def crear_reserva(self, usuario, fecha, hora, numero_personas):
        if not self.verificar_disponibilidad(fecha, hora, numero_personas):
            raise ValueError("No hay disponibilidad para esta fecha y hora.")
        reserva = Reserva(usuario, fecha, hora, numero_personas)
        self.reservas.append(reserva)

    def cancelar_reserva(self, usuario, fecha, hora):
        self.reservas = [reserva for reserva in self.reservas if not (reserva.usuario == usuario and reserva.fecha == fecha and reserva.hora == hora)]

    def verificar_disponibilidad(self, fecha, hora, numero_personas):
        total_personas = sum([reserva.numero_personas for reserva in self.reservas if reserva.fecha == fecha and reserva.hora == hora])
        capacidad_maxima = 50  # Definimos que el restaurante tiene una capacidad máxima de 50 personas por hora
        return total_personas + numero_personas <= capacidad_maxima

    def listar_reservas_usuario(self, usuario):
        return [reserva for reserva in self.reservas if reserva.usuario == usuario]


