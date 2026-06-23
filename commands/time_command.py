import datetime

from voice.speech import falar


def falar_hora():

    agora = datetime.datetime.now()

    hora = agora.hour
    minuto = agora.minute

    falar(f"Agora são {hora} horas e {minuto} minutos")