import webbrowser

from voice.speech import falar


def abrir_youtube():

    falar("Abrindo YouTube")

    webbrowser.open("https://youtube.com")