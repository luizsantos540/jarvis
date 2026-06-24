from voice.speech import falar
from voice.listener import ouvir
from commands.actions import executar_comando

falar("DEX iniciado. Pode falar.")

ativa = True

while ativa:
    
    comando = ouvir()

    if not comando:
        continue

    comando = comando.lower().strip()

    
    if "desligar assistente" in comando or "encerrar" in comando:
        falar("Desligando os sistemas. Até mais.")
        ativa = False
        break

    
    ativa = executar_comando(comando)