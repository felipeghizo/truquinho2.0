class Truco2:

    def __init__(self, truco1):

        self.truco1 = truco1


    def truc(self, truco1):

        aux_truco = []
        lista = []
        pontos = 1
        win_mao2 = 0

        if truco1[0] == "S":
            resp2 = int(input("Desejas: [1] Correr [2] cair [3] Pedir seis \n"))
            if resp2 == 1:
                pontos = 1
                win_mao2 = 2
                print(f"Jogador 2 levou a rodada valendo 1 ponto.")
                lista.append(win_mao2)
                lista.append(pontos)

                return lista

            if resp2 == 2:
                print("agora a rodada vale 3 pontos!")
                pontos = 3

                lista.append(win_mao2)
                lista.append(pontos)

                return lista

            if resp2 == 3:

                return Seis2.seis2(self, "S")


        else:
            pontos = 1

        lista. append(win_mao2)
        lista.append(pontos)

        return lista


class Seis2(Truco2):

    def __init__(self, truco1, seis):

        Truco2.__init__(self, truco1)
        self.seis = seis

    def seis2(self, seis):

        pontos = 3

        lista = []
        win_mao1 = 0

        if pontos == 3:
            if seis[0] == "S":
                resp1 = int(input("Desejas: [1] Correr(oponente ganha 3 pontos) [2] cair(a rodada vale 6 pontos) [3] Pedir nove\n"))
                if resp1 == 1:
                    lista.append(2)
                    lista.append(3)
                    print(f"Jogador 1' levou a rodada valendo 3 pontos.")
                    return lista

                if resp1 == 2:
                    print("agora a rodada vale 6 pontos!")

                    lista.append(0)
                    lista.append(6)
                    return lista

                if resp1 == 3:

                    return Nove2.nove2(self, "S")
            else:
                pontos = 3

        lista.append(win_mao1)
        lista.append(pontos)

        return lista


class Nove2(Seis2):

    def __init__(self, truco1, seis, nove):

        Seis2.__init__(self, truco1, seis)
        self.nove = nove

    def nove2(self, nove):

        lista = []
        pontos = 6
        win_mao2 = 0

        if pontos == 6:
            if nove[0] == "S":
                resp22 = int(input("Desejas: [1] Correr(oponente ganha 6 pontos) [2] cair(a rodada vale 9 pontos) [3] Pedir doze\n"))
                if resp22 == 1:

                    lista.append(2)
                    lista.append(6)
                    print(f"Jogador 2 levou a rodada valendo 6 pontos.")
                    return lista

                if resp22 == 2:
                    print("agora a rodada vale 9 pontos!")
                    pontos = 9
                    lista.append(0)
                    lista.append(9)
                    return lista

                if resp22 == 3:

                    return Doze2.doze2(self, "S")
            else:
                pontos = 6

        lista. append(win_mao2)
        lista.append(pontos)

        return lista


class Doze2(Nove2):

    def __init__(self, truco1, seis, nove, doze):

        Nove2.__init__(self, truco1, seis, nove)
        self.doze = doze

    def doze2(self, doze):

        lista = []
        pontos = 9
        win_mao1 = 0

        if pontos == 9:
            if doze[0] == "S":
                resp11 = int(input("Desejas: [1] Correr(oponente ganha 9 pontos) [2] cair(a rodada vale 12 pontos)\n"))
                if resp11 == 1:
                    lista.append(2)
                    lista.append(9)
                    print(f"Jogador 1 levou a rodada valendo 9 pontos.")
                    return lista

                if resp11 == 2:
                    print("agora a rodada vale 12 pontos!")

                    lista.append(0)
                    lista.append(12)
                    return lista
            else:
                pontos = 9

        lista. append(win_mao1)
        lista.append(pontos)

        return lista







