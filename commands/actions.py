import unicodedata
from commands.greeting import responder_ola
from commands.time_command import falar_hora
from commands.browser import abrir_youtube
from commands.system_apps import abrir_calculadora, abrir_bloco_de_notas
from commands.google_search import pesquisar_google
from commands.question_answer import responder_pergunta
from commands.monitor import checar_sistema, checar_bitcoin
from voice.speech import falar


def remover_acentos(texto):
    return "".join(
        caractere
        for caractere in unicodedata.normalize("NFD", texto)
        if unicodedata.category(caractere) != "Mn"
    )


def executar_comando(comando):
    comando = comando.lower()
    comando = remover_acentos(comando)

    print(f"Comando recebido: {comando}")

    if "ola" in comando:
        responder_ola()

    elif "hora" in comando:
        falar_hora()

    elif "youtube" in comando:
        abrir_youtube()

    elif "calculadora" in comando:
        abrir_calculadora()

    elif "bloco de notas" in comando:
        abrir_bloco_de_notas()

    elif "sistema" in comando or "hardware" in comando:
        checar_sistema()

    elif "bitcoin" in comando or "cripto" in comando:
        checar_bitcoin()

    elif "pesquise" in comando:
        termo = comando
        termo = termo.replace("pesquise por", "")
        termo = termo.replace("pesquise", "")
        termo = termo.replace("no google", "")
        termo = termo.strip()
        pesquisar_google(termo)

    elif "encerrar" in comando:
        falar("Encerrando Jarvis.")
        return False

    else:
        falar("Comando nao reconhecido.")

    return True