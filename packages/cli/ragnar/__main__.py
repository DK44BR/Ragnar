import sys

from ragnar.commands.doctor import doctor
from ragnar.commands.esp import list_devices, build, flash, monitor, info


def main():

    if len(sys.argv) < 2:
        print("""
===================================
        RAGNAR CLI v0.1
===================================

Uso:

ragnar doctor

ragnar esp list
ragnar esp build
ragnar esp flash
ragnar esp monitor

""")
        return


    comando = sys.argv[1]


    if comando == "doctor":

        doctor()


    elif comando == "esp":

        if len(sys.argv) < 3:
            print("Use: ragnar esp [list|build|flash|monitor]")
            return


        acao = sys.argv[2]


        if acao == "list":
            list_devices()

        elif acao == "build":
            build()

        elif acao == "flash":
            flash()

        elif acao == "monitor":
            monitor()

        elif acao == "info":
            info()

        else:
            print("Comando ESP desconhecido")


    else:

        print("Comando desconhecido:", comando)



if __name__ == "__main__":
    main()
