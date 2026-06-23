from plyer import notification
import psutil
import requests
from voice.speech import falar


def checar_sistema():
    uso_cpu = psutil.cpu_percent(interval=1)
    uso_memoria = psutil.virtual_memory().percent

    falar(f"O uso da CPU esta em {uso_cpu} por cento e a memoria em {uso_memoria} por cento.")

    limite = 80.0
    if uso_cpu > limite or uso_memoria > limite:
        notification.notify(
            title="Alerta de Hardware",
            message=f"CPU: {uso_cpu}% | RAM: {uso_memoria}%",
            app_name="Jarvis",
            timeout=5,
        )


def checar_bitcoin():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        resposta = requests.get(url)
        dados = resposta.json()
        preco = dados.get("bitcoin", {}).get("usd")

        falar(f"O preco atual do Bitcoin e de {preco} dolares.")

    except Exception:
        falar("Nao consegui acessar a cotacao do Bitcoin no momento.")