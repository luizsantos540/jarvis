import speech_recognition as sr


recognizer = sr.Recognizer()


def ouvir():

    with sr.Microphone() as source:

        print("Jarvis está ouvindo...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        comando = recognizer.recognize_google(
            audio,
            language="pt-BR"
        )

        print(f"Você disse: {comando}")

        return comando

    except sr.UnknownValueError:
        print("Não entendi o que você disse.")

    except sr.RequestError:
        print("Erro ao conectar com o serviço de voz.")

    return ""