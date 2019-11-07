class Automato:
    def __init__(self, qtd_estados, estados_finais, *args):

        # Criando uma lista de dicionários, onde cada indice da lista, corresponde a
        # um estado, e cada dicionário correspondente contém as transições desse estado.
        self.transicoes = [{} for i in range(qtd_estados)]

        # Atribuindo funções de transição recebidas ao dicionário
        for t in args:
            for v in t[1]:
                self.transicoes[t[0]][v] = t[2]

        # Criando uma lista de booleanos com a mesma quantidade de estados,
        # onde cada indice corresponde a um estado.
        # Sendo True para um estado final e False para um estado não final.
        self.estados_finais = [False] * qtd_estados
        for f in estados_finais:
            self.estados_finais[f] = True

    def retorna_cadeia(self, cadeia):
        estado = 0
        caracter_final = 0
        try:
            for c in cadeia:
                estado = self.transicoes[estado][c]
                caracter_final += 1
            return caracter_final
        except KeyError:
            return caracter_final


# Alfabeto (maiúsculo e minúsculo)
alfabeto = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

# Números de 0-9
numeros = [chr(i) for i in range(48, 58)]

# Instância dos Automatos
AF_identificador = Automato(2, [1], (0, alfabeto, 1), (1, alfabeto + numeros, 1))
AF_soma = Automato(2, [1], (0, ['+'], 1))
AF_subt = Automato(2, [1], (0, ['-'], 1))
AF_divi = Automato(2, [1], (0, ['/'], 1))
AF_mult = Automato(2, [1], (0, ['*'], 1))

# Lendo arquivo de entrada input.txt
with open('input.txt', 'r') as file:
    instrucoes = file.read()

# Gerando tokens a partir dos automatos
tokens = []

# Percorrendo o input.txt e reconhecendo os automatos
while instrucoes:
    palavra = instrucoes[:AF_identificador.retorna_cadeia(instrucoes)]
    if palavra:
        tokens.append(f'<identificador, {palavra}>\n')
        instrucoes = instrucoes[AF_identificador.retorna_cadeia(instrucoes):]
        continue

    palavra = instrucoes[:AF_soma.retorna_cadeia(instrucoes)]
    if palavra:
        tokens.append(f'<soma,>\n')
        instrucoes = instrucoes[AF_soma.retorna_cadeia(instrucoes):]
        continue

    palavra = instrucoes[:AF_subt.retorna_cadeia(instrucoes)]
    if palavra:
        tokens.append(f'<sub,>\n')
        instrucoes = instrucoes[AF_subt.retorna_cadeia(instrucoes):]
        continue

    palavra = instrucoes[:AF_divi.retorna_cadeia(instrucoes)]
    if palavra:
        tokens.append(f'<div,>\n')
        instrucoes = instrucoes[AF_divi.retorna_cadeia(instrucoes):]
        continue

    palavra = instrucoes[:AF_mult.retorna_cadeia(instrucoes)]
    if palavra:
        tokens.append(f'<mult,>\n')
        instrucoes = instrucoes[AF_mult.retorna_cadeia(instrucoes):]
        continue

    instrucoes = instrucoes[1:]


# Escrevendo no arquivo output.txt.
with open('output.txt', 'w') as file:
    file.writelines(tokens)
