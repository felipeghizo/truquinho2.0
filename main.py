from random import randint
import time
from PROJETO.TRUCO1 import Truco1, Seis1, Nove1, Doze1
from PROJETO.TRUCO2 import Truco2, Seis2, Nove2, Doze2
'''from PROJETO.SEIS import Seis1
from PROJETO.NOVE import Nove1
from PROJETO.DOZE import Doze1'''
from PROJETO.PODER_TOTAL_BARALHO import Poder


class Main:
    def __init__(self):
        pontos_totais1 = 0
        pontos_totais2 = 0
        pontos = 1
        tot = False

        while tot != True:

            cartas = ["4", "5", "6", "7", "10", "11", "12", "1", "2", "3"]
            nipes = ["moles", "espadas", "copas", "paus"]

            aux_baralho_total = []

            for j in range(0, 10):
                for i in range(0, 4):
                    aux_baralho_total.append(cartas[j])
                    aux_baralho_total.append(nipes[i])

            for q in range(3):
                primeiro1 = 0
                primeiro2 = 0
                aux_get = []

                win_mao1 = 0
                win_mao2 = 0

                mao1 = []
                mao2 = []
                for v in range(3):
                    get_carta1 = randint(0, 78)

                    while True:                                                         #definindo a mao 1. serve para que nao caiam cartas iguais.
                        if get_carta1 % 2 == 0:
                            if get_carta1 not in aux_get:
                                mao1.append(aux_baralho_total[get_carta1])
                                mao1.append(aux_baralho_total[get_carta1 + 1])
                                aux_get.append(get_carta1)
                                break
                            else:
                                get_carta1 = randint(0, 78)
                        else:
                            get_carta1 = randint(0, 78)

                    get_carta2 = randint(0, 78)

                    while True:                                                         #definindo a mao 2. serve para que nao caiam cartas iguais.
                        if get_carta2 % 2 == 0:
                            if get_carta2 not in aux_get:
                                mao2.append(aux_baralho_total[get_carta2])
                                mao2.append(aux_baralho_total[get_carta2 + 1])
                                aux_get.append(get_carta2)
                                break
                            else:
                                get_carta2 = randint(0, 78)
                        else:
                            get_carta2 = randint(0, 78)

                while True:
                    coringa_aux = randint(0, 78)
                    if coringa_aux not in aux_get:
                        if coringa_aux % 2 == 0:
                            if aux_baralho_total[coringa_aux] == "12":
                                coringa = "1"
                                break
                            elif aux_baralho_total[coringa_aux] == "7":
                                coringa = "10"
                                break
                            elif aux_baralho_total[coringa_aux] == "3":
                                coringa = "4"
                                break
                            else:
                                coringa = (aux_baralho_total[coringa_aux + 2])
                                break
                        else:
                            coringa_aux = randint(0, 78)
                    else:
                        coringa_aux = randint(0, 78)


                print("mao1:", mao1)
                print("mao2:", mao2)
                print("coringa", coringa)

                aux_poder_baralho = Poder.pod(self, coringa, aux_baralho_total)

                totaux = False
                while totaux is False:
                    for u in range(3):
                        print(u)
                        aux_truco = []
                        aux_truco6 = []
                        aux_truco9 = []
                        aux_truco12 = []

                        aux_truco2 = []
                        aux_truco26 = []
                        aux_truco29 = []
                        aux_truco212 = []
                        truco3 = False
                        truco6 = False
                        truco9 = False
                        truco12 = False
                        ################################################################################    CARTA JOGADA PELA MAO 1
                        print(mao1)
                        if truco3 is False:
                            truco1 = input("pedir truco?").upper().strip()
                            if truco1[0] == "S":
                                truco3 = True
                            aux_truco.append(Truco1.truc(self, truco1))
                            print(aux_truco)
                            win_mao1 = aux_truco[0][0]
                            pontos = aux_truco[0][1]
                            if win_mao1 == 2:
                                truco3 = True
                                totaux = True
                                break
                            if pontos == 3:
                                truco3 = True

                        elif truco6 is False:
                            seis = input("pedir seis?").upper().strip()
                            if seis[0] == "S":
                                truco6 = True
                            aux_truco6.append(Seis1.seis1(self, seis))
                            print(aux_truco6)
                            win_mao1 = aux_truco6[0][0]
                            pontos = aux_truco6[0][1]

                            if win_mao1 == 2:
                                truco6 = True
                                totaux = True
                                break

                            if pontos == 6:
                                truco6 = True

                        elif truco9 is False:
                            nove = input("pedir nove?").upper().strip()
                            if nove[0] == "S":
                                truco9 = True
                            aux_truco9.append(Nove1.nove1(self, nove))
                            print(aux_truco9)
                            win_mao2 = aux_truco9[0][0]
                            pontos = aux_truco6[0][1]
                            if win_mao2 == 2:
                                truco9 = True
                                totaux = True
                                break

                            if pontos == 9:
                                truco9 = True

                        elif truco12 is False:
                            doze = input("pedir doze?").upper().strip()
                            if doze[0] == "S":
                                truco12 = True
                            aux_truco12.append(Doze1.doze1(self, doze))
                            pontos = aux_truco6[0][1]
                            if win_mao1 == 2:
                                truco12 = True
                                totaux = True
                                break

                            if pontos == 12:
                                truco12 = True


                        mao1_PLAY_num = input("Qual o numero da carta que desejas jogar ?")
                        while True:
                            if mao1_PLAY_num not in mao1:
                                mao1_PLAY_num = input("Voce nao possui essa carta! Tente novamente:")
                            else:
                                break

                        mao1_PLAY_nipe = input("Qual o nipe da carta que desejas jogar ?")
                        while True:
                            if mao1_PLAY_nipe not in mao1:
                                mao1_PLAY_nipe = input("Voce nao possui essa carta! Tente novamente:")
                            else:
                                break

                        ###############################################################################     USAR A POSIÇAO PARA DEFINIR O VALOR
                        for t in range(80):
                            if (mao1_PLAY_num == aux_poder_baralho[t]):
                                pos_mao1_PLAY_num = t

                            if (mao1_PLAY_num == aux_poder_baralho[t]) and (mao1_PLAY_nipe == (aux_poder_baralho[t + 1])) and t >= 72:
                                pos_mao1_PLAY_num = t
                                pos_mao1_PLAY_nipe = t + 1
                                break


                        for i in range(0, len(mao1), 2):
                            if mao1_PLAY_num == mao1[i] and mao1_PLAY_nipe == mao1[i + 1]:
                                mao1.pop(i + 1)
                                mao1.pop(i)
                                break
                            else:
                                print('')

                        #############################################################################   CARTA JOGADA PELA MÃO 2
                        print(mao2)
                        if truco3 is False:
                            truco1 = input("pedir truco?").upper().strip()
                            if truco1[0] == "S":
                                truco3 = True
                            aux_truco2.append(Truco2.truc(self, truco1))
                            win_mao2 = aux_truco2[0][0]
                            pontos = aux_truco2[0][1]
                            if win_mao2 == 2:
                                truco3 = True
                                totaux = True
                                break

                            if pontos == 3:
                                truco3 = True


                        elif truco6 is False:
                            seis = input("pedir seis?").upper().strip()
                            if seis[0] == "S":
                                truco6 = True
                            aux_truco26.append(Seis2.seis2(self, seis))
                            win_mao1 = aux_truco26[0][0]
                            pontos = aux_truco26[0][1]
                            if win_mao1 == 2:
                                truco6 = True
                                totaux = True
                                break

                            if pontos == 6:
                                truco6 = True


                        elif truco6 is False:
                            nove = input("pedir nove?").upper().strip()
                            if nove[0] == "S":
                                truco9 = True
                            aux_truco29.append(Nove2.nove2(self, nove))
                            win_mao2 = aux_truco29[0][0]
                            pontos = aux_truco29[0][1]
                            if win_mao2 == 2:
                                truco9 = True
                                totaux = True
                                break

                            if pontos == 9:
                                truco9 = True


                        elif truco12 is False:
                            doze = input("pedir doze?").upper().strip()
                            if doze[0] == "S":
                                truco12 = True
                            aux_truco212.append(Doze2.doze2(self, doze))
                            win_mao1 = aux_truco212[0][0]
                            pontos = aux_truco212[0][1]
                            if win_mao1 == 2:
                                truco12 = True
                                totaux = True
                                break

                            if pontos == 12:
                                truco12 = True

                        mao2_PLAY_num = input("Qual o numero da carta que desejas jogar ?")
                        while True:
                            if mao2_PLAY_num not in mao2:
                                mao2_PLAY_num = input("Voce nao possui essa carta! Tente novamente:")
                            else:
                                break

                        mao2_PLAY_nipe = input("Qual o nipe da carta que desejas jogar ?")
                        while True:
                            if mao2_PLAY_nipe not in mao2:
                                mao2_PLAY_nipe = input("Voce nao possui essa carta! Tente novamente:")
                            else:
                                break
                        #  truco_mao2 = input("Desejas Trucar ?").upper().strip()

                        ############################################################################   PEGAR A POSIÇÃO E O VALOR DAS CARTAS

                        for t in range(len(aux_poder_baralho)):
                            if (mao2_PLAY_num == aux_poder_baralho[t]):
                                pos_mao2_PLAY_num = t

                            if (mao2_PLAY_num == aux_poder_baralho[t]) and (mao2_PLAY_nipe == (aux_poder_baralho[t + 1])) and t >= 72:
                                pos_mao2_PLAY_num = t
                                pos_mao2_PLAY_nipe = t + 1

                        for i in range(0, len(mao2), 2):
                            if mao2_PLAY_num == mao2[i] and mao2_PLAY_nipe == mao2[i + 1]:
                                mao2.pop(i + 1)
                                mao2.pop(i)
                                break
                            else:
                                print('')

                        ############################################################################# APLICAR A PONTUAÇÃO AO VENCEDOR OU AO ENPATE
                        if pos_mao1_PLAY_num > pos_mao2_PLAY_num:
                            win_mao1 += 1
                            if u == 0:
                                primeiro1 = 1
                            print(f"Jogador 1 levou a {u + 1}ª rodada.")

                        elif pos_mao1_PLAY_num < pos_mao2_PLAY_num:
                            win_mao2 += 1
                            if u == 0:
                                primeiro2 = 1
                            print(f"Jogador 2 levou a {u + 1}ª rodada.")


                        elif pos_mao1_PLAY_num == pos_mao2_PLAY_num:
                            if primeiro1 == 0 and primeiro2 == 0:
                                win_mao1 += 1
                                win_mao2 +=1
                                print(f"A {u + 1}ª rodada embuxou.")

                            if primeiro1 == 1:
                                print(f"Jogador 1 levou a {u + 1}ª rodada.")
                            if primeiro2 == 1:
                                print(f"Jogador 2 levou a {u + 1}ª rodada.")

                        elif pos_mao1_PLAY_num >= 72 and  pos_mao1_PLAY_num >= 72:
                            if pos_mao1_PLAY_nipe > pos_mao2_PLAY_nipe:
                                win_mao1 += 1
                                print(f"Jogador 1 levou a {u + 1}ª rodada.")

                            else:
                                win_mao2 += 1
                                print(f"Jogador 2 levou a {u + 1}ª rodada.")

                    if win_mao1 == 2:

                        pontos_totais1 += pontos
                        print(f"O jogador 1 levou a melhor de 3.")
                        print(f"placar: \n jogador1: {pontos_totais1} \n jogador2: {pontos_totais2}")
                        time.sleep(2)

                        if pontos_totais1 == 12:
                            dic = {"1ª lugar": "jogador 1", "2ª lugar": "jogador 2"}
                            print(dic)
                            tot = True
                            totaux = True
                            break

                    if win_mao2 == 2:
                        pontos_totais2 += pontos
                        print(f"O jogador 2 levou a melhor de 3.")
                        print(f"placar: \n jogador1: {pontos_totais1} \n jogador2: {pontos_totais2}")
                        time.sleep(2)
                        if pontos_totais2 == 12:
                            dic = {"1ª lugar": "jogador 2", "2ª lugar": "jogador 1"}
                            print(dic)
                            tot = True
                            totaux = True
                            break
            if pontos_totais2 == 12 or pontos_totais1 == 12:
                break





Main()
