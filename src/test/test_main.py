import pytest
from ..main import SistemaReservas

def test_crear_reserva():
    sistema = SistemaReservas()
    sistema.crear_reserva("usuario1", "2024-10-15", "20:00", 4)
    assert len(sistema.reservas) == 1

def test_crear_reserva_sin_disponibilidad():
    sistema = SistemaReservas()
    sistema.crear_reserva("usuario1", "2024-10-15", "20:00", 48)  
    with pytest.raises(ValueError):
        sistema.crear_reserva("usuario2", "2024-10-15", "20:00", 3) 

def test_cancelar_reserva():
    sistema = SistemaReservas()
    sistema.crear_reserva("usuario1", "2024-10-15", "20:00", 4)
    sistema.cancelar_reserva("usuario1", "2024-10-15", "20:00")
    assert len(sistema.reservas) == 0

def test_cancelar_reserva_no_existente():
    sistema = SistemaReservas()
    sistema.crear_reserva("usuario1", "2024-10-15", "20:00", 4)
    sistema.cancelar_reserva("usuario2", "2024-10-15", "20:00")  # No existe para usuario2
    assert len(sistema.reservas) == 1  # La reserva original sigue existiendo

def test_verificar_disponibilidad():
    sistema = SistemaReservas()
    sistema.crear_reserva("usuario1", "2024-10-15", "20:00", 45)  # Casi lleno
    assert sistema.verificar_disponibilidad("2024-10-15", "20:00", 5) is False  # No hay disponibilidad
    assert sistema.verificar_disponibilidad("2024-10-15", "20:00", 4) is True  # Exactamente lo que queda

def test_listar_reservas_usuario():
    sistema = SistemaReservas()
    sistema.crear_reserva("usuario1", "2024-10-15", "20:00", 4)
    sistema.crear_reserva("usuario1", "2024-10-16", "19:00", 2)
    sistema.crear_reserva("usuario2", "2024-10-15", "20:00", 5)
    reservas_usuario1 = sistema.listar_reservas_usuario("usuario1")
    assert len(reservas_usuario1) == 2
    assert reservas_usuario1[0].fecha == "2024-10-15"
    assert reservas_usuario1[1].fecha == "2024-10-16"





