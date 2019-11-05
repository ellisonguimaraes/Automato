class Automato:
    def __init__(self, qtd_estados, estados_finais, *args):

        # Criando uma lista de dicionários com transições
        self.transicoes = [{} for i in range(qtd_estados)]

        # Atribuindo funções de transição
        for t in args:
            for v in t[1]:
                self.transicoes[t[0]][v] = t[2]

        # Uma lista de estados_finais (True e False)
        self.estados_finais = [False] * qtd_estados

        # Colocando como True os estados finais
        for f in estados_finais:
            self.estados_finais[f] = True

    def aceita_cadeia(self, cadeia):
        estado = 0
        try:
            for c in cadeia:
                estado = self.transicoes[estado][c]
            return self.estados_finais[estado]
        except KeyError:
            return False


alfabeto = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
numeros = [chr(i) for i in range(48, 58)]

AF_identificador = Automato(2, [1], (0, alfabeto, 1), (1, alfabeto + numeros, 1))
AF_soma = Automato(2, [1], (0, ['+'], 1))
AF_subt = Automato(2, [1], (0, ['-'], 1))
AF_divi = Automato(2, [1], (0, ['/'], 1))
AF_mult = Automato(2, [1], (0, ['*'], 1))


with open('input.txt', 'r') as file:
    instrucoes = file.read().split()


tokens = []

for palavra in instrucoes:

    if AF_identificador.aceita_cadeia(palavra):
        tokens.append(f'<identificador, {palavra}>\n')
        continue

    if AF_soma.aceita_cadeia(palavra):
        tokens.append(f'<soma,>\n')
        continue

    if AF_subt.aceita_cadeia(palavra):
        tokens.append(f'<sub,>\n')
        continue

    if AF_divi.aceita_cadeia(palavra):
        tokens.append(f'<div,>\n')
        continue

    if AF_mult.aceita_cadeia(palavra):
        tokens.append(f'<mult,>\n')
        continue


with open('output.txt', 'w') as file:
    file.writelines(tokens)


AF_identificador.aceita_cadeia('var')
AF_identificador.aceita_cadeia('6car')
AF_soma.aceita_cadeia('+')
AF_soma.aceita_cadeia('-')