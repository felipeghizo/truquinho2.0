class Poder:

    def pod(self, coringa, aux_baralho_total):

        self.coringa = coringa
        self.aux_baralho_total = aux_baralho_total

        poder_baralho = []
        coringuinha = []
        aux_poder_baralho = []

        for x in range(80):
            if self.coringa != self.aux_baralho_total[x] and x % 2 == 0:
                poder_baralho.append(self.aux_baralho_total[x])
                poder_baralho.append(self.aux_baralho_total[x + 1])

        for x in range(80):
            if self.coringa == self.aux_baralho_total[x] and x % 2 == 0:
                coringuinha.append(self.coringa)
                coringuinha.append(self.aux_baralho_total[x + 1])

        for x in range(80):
            if x < 72:
                aux_poder_baralho.append(poder_baralho[x])
            else:
                for y in range(8):
                    aux_poder_baralho.append(coringuinha[y])
                break

        return aux_poder_baralho
