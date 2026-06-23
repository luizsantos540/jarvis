from voice.speech import falar
from voice.listener import ouvir
from commands.actions import executar_comando


falar("Jarvis iniciada com sucesso.")

ativa = True


while ativa:

    comando = ouvir()

    if not comando:
        continue

    comando = comando.lower()

    if "jarvis" in comando:

        comando = comando.replace("jarvis", "").strip()

        ativa = executar_comando(comando)