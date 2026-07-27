import subprocess


def list_devices():

    print("=== Ragnar ESP Scanner ===")

    resultado = subprocess.run(
        ["pio", "device", "list"],
        capture_output=True,
        text=True
    )

    print(resultado.stdout)


def build():

    print("Compilando firmware...")

    subprocess.run(
        ["pio", "run"]
    )


def flash():

    print("Enviando firmware para ESP32...")

    subprocess.run(
        [
            "pio",
            "run",
            "-t",
            "upload"
        ]
    )


def monitor():

    print("Abrindo monitor serial...")

    subprocess.run(
        [
            "pio",
            "device",
            "monitor",
            "-b",
            "115200"
        ]
    )


def info():

    print("""
================================
       RAGNAR ESP INFO
================================
""")

    resultado = subprocess.run(
        ["pio", "device", "list"],
        capture_output=True,
        text=True
    )

    if "ttyUSB" in resultado.stdout or "ttyACM" in resultado.stdout:

        for linha in resultado.stdout.splitlines():

            if "ttyUSB" in linha or "ttyACM" in linha:
                print("Porta encontrada:")
                print(linha)

        print("")
        print("Status: Conectado")

    else:

        print("Nenhuma ESP encontrada")

    print("""
================================
""")
