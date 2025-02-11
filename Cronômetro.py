import time

def cronometro():
    horas = 0
    minutos = 0
    segundos = 0

    while True:
        time.sleep(1)
        segundos += 1

        if segundos == 60:
            segundos = 0
            minutos += 1

        if minutos == 60:
            minutos = 0
            horas += 1

        print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

cronometro()