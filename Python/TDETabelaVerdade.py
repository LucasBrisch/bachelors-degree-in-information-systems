class TabelaVerdade:
    def __init__(self, equacao):
        self.equacao = equacao
        self.tabela = []

    def gerar_tabela(self):
        for p in [False, True]:
            for q in [False, True]:
                resultado = eval(self.equacao, {'P': p, 'Q': q})
                self.tabela.append([p, q, resultado])

    def exibir_tabela(self):
        print("P | Q | Resultado")
        print("-" * 13)
        for linha in self.tabela:
            p, q, resultado = linha
            print(f"{int(p)} | {int(q)} | {int(resultado)}")

equacao = input("Digite a equação (utilize P e Q como variáveis): ")
tabela_verdade = TabelaVerdade(equacao)
tabela_verdade.gerar_tabela()
tabela_verdade.exibir_tabela()