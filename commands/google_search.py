import webbrowser

from voice.speech import falar


def pesquisar_google(termo):

    falar(f"Pesquisando por {termo}")

    url = f"https://www.google.com/search?q={termo}"

    webbrowser.open(url)