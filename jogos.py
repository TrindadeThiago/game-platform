import forca
import adiviacao


def escolhe_jogo():
    print("************************************")
    print("********* Escolha seu jogo *********")
    print("************************************")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Escolha o jogo: "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    else:
        print("Jogando adivinhação")
        adiviacao.jogar()


if (__name__ == "__main__"):
    escolhe_jogo()
