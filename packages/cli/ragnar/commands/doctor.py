import platform
import shutil


def doctor():

    print("")
    print("=== Ragnar System Check ===")
    print("Sistema:", platform.system())
    print("Python:", platform.python_version())
    print("")


    ferramentas = [
        "git",
        "python3",
        "pio",
        "arduino-cli",
        "docker"
    ]


    for ferramenta in ferramentas:

        if shutil.which(ferramenta):
            print("[OK] ", ferramenta)

        else:
            print("[--] ", ferramenta)


    print("")
    print("==========================")
