import subprocess

from voice.speech import falar


def abrir_calculadora():

    falar("Abrindo calculadora")

    subprocess.Popen("calc.exe")


def abrir_bloco_de_notas():

    falar("Abrindo bloco de notas")

    subprocess.Popen("notepad.exe")