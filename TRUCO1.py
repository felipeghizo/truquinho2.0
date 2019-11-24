<<<<<<< HEAD
class Truco1:

    def __init__(self, truco1):

        self.truco1 = truco1


    def truc(self, truco1):

=======
from SEIS import Seis1


class Truco1():

    def truc(self, truco1):

        self.truco1 = truco1
>>>>>>> parent of f446c42... blablabla
        aux_truco = []
        lista = []
        pontos = 1
        win_mao1 = 0

<<<<<<< HEAD
        if truco1[0] == "S":
=======
        if self.truco1[0] == "S":
>>>>>>> parent of f446c42... blablabla
            resp2 = int(input("Desejas: [1] Correr [2] cair [3] Pedir seis \n"))
            if resp2 == 1:
                pontos = 1
                win_mao1 = 2
                print(f"Jogador 1 levou a rodada valendo 1 ponto.")
                lista.append(win_mao1)
                lista.append(pontos)

                return lista

            if resp2 == 2:
<<<<<<< HEAD
                print("agora a rodada vale 3 pontos!")
=======
>>>>>>> parent of f446c42... blablabla
                pontos = 3

                lista.append(win_mao1)
                lista.append(pontos)

                return lista

            if resp2 == 3:
<<<<<<< HEAD

                return Seis1.seis1(Truco1, "S")


        else:
            pontos = 1

        lista. append(win_mao1)
        lista.append(pontos)

        return lista


class Seis1(Truco1):

    def __init__(self, truco1, seis):

        Truco1.__init__(self, truco1)
        self.seis = seis

    def seis1(self, seis):

        pontos = 3

        lista = []
        win_mao2 = 0

        if pontos == 3:
            if seis[0] == "S":
                resp1 = int(input("Desejas: [1] Correr(oponente ganha 3 pontos) [2] cair(a rodada vale 6 pontos) [3] Pedir nove\n"))
                if resp1 == 1:
                    lista.append(2)
                    lista.append(3)
                    print(f"Jogador 2 levou a rodada valendo 3 pontos.")
                    return lista

                if resp1 == 2:
                    print("agora a rodada vale 6 pontos!")

                    lista.append(0)
                    lista.append(6)
                    return lista

                if resp1 == 3:

                    return Nove1.nove1(Truco1, "S")
            else:
                pontos = 3

        lista.append(win_mao2)
        lista.append(pontos)

        return lista


class Nove1(Seis1):

    def __init__(self, truco1, seis, nove):

        Seis1.__init__(self, truco1, seis)
        self.nove = nove

    def nove1(self, nove):

        lista = []
        pontos = 6
        win_mao1 = 0

        if pontos == 6:
            if nove[0] == "S":
                resp22 = int(input("Desejas: [1] Correr(oponente ganha 6 pontos) [2] cair(a rodada vale 9 pontos) [3] Pedir doze\n"))
                if resp22 == 1:

                    lista.append(2)
                    lista.append(6)
                    print(f"Jogador 1 levou a rodada valendo 6 pontos.")
                    return lista

                if resp22 == 2:
                    print("agora a rodada vale 9 pontos!")
                    pontos = 9
                    lista.append(0)
                    lista.append(9)
                    return lista

                if resp22 == 3:

                    return Doze1.doze1(self, "S")
            else:
                pontos = 6

        lista. append(win_mao1)
        lista.append(pontos)

        return lista


class Doze1(Nove1):

    def __init__(self, truco1, seis, nove, doze):

        Nove1.__init__(self, truco1, seis, nove)
        self.doze = doze

    def doze1(self, doze):

        lista = []
        pontos = 9
        win_mao2 = 0

        if pontos == 9:
            if doze[0] == "S":
                resp11 = int(input("Desejas: [1] Correr(oponente ganha 9 pontos) [2] cair(a rodada vale 12 pontos)\n"))
                if resp11 == 1:
                    lista.append(2)
                    lista.append(9)
                    print(f"Jogador 2 levou a rodada valendo 9 pontos.")
                    return lista

                if resp11 == 2:
                    print("agora a rodada vale 12 pontos!")

                    lista.append(0)
                    lista.append(12)
                    return lista
            else:
                pontos = 9

        lista. append(win_mao2)
        lista.append(pontos)

        return lista
=======
                aux_truco.append(Seis1.seis1(self, pontos, " "))
                lista.append(aux_truco[0][0])
                lista.append(aux_truco[0][1])

                return lista
        else:
            pontos = 1

            lista. append(win_mao1)
            lista.append(pontos)

            return lista



>>>>>>> parent of f446c42... blablabla



















