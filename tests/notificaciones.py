from src.notificaciones import enviar_notificacion

def test_enviar_notificacion():
    assert enviar_notificacion("Daniel", "Tienes una nueva tarea") == "Notificación enviada a Daniel: Tienes una nueva tarea"
    assert enviar_notificacion("", "Mensaje") == "Error: datos incompletos"
    assert enviar_notificacion("Daniel", "") == "Error: datos incompletos"
    