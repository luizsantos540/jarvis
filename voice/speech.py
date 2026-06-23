import pyttsx3


def falar(texto):

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    voz_escolhida = voices[0]

    engine.setProperty('voice', voz_escolhida.id)

    engine.setProperty('rate', 180)

    engine.setProperty('volume', 1.0)

    print(f"Jarvis irá falar: {texto}")

    engine.say(texto)

    engine.runAndWait()

    engine.stop()