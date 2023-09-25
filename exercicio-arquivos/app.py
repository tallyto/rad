import codecs

def gravaNotasAV3(linha):
    with codecs.open('fizeramAV3.txt', 'a', 'utf-8') as arquivoNotas:
        arquivoNotas.write(linha)

def calcularMediaImprime(dados_alunos):
    for nome, notas in dados_alunos.items():
        notas_float = [float(nota) for nota in notas]
        media = sum(notas_float) / len(notas_float)
        print(f'Média de {nome}: {media:.2f}')

def calcularMinimaMaxima(dados_alunos):
    for nome, notas in dados_alunos.items():
        notas_float = [float(nota) for nota in notas]
        nota_minima = min(notas_float)
        nota_maxima = max(notas_float)
        print(f'Aluno: {nome}, Nota Mínima: {nota_minima:.2f}, Nota Máxima: {nota_maxima:.2f}')

dados_alunos = {}

with codecs.open('notas.txt', 'r', 'utf-8') as arquivo:
    for linha in arquivo:
        linhaLimpa = linha.strip().split(';')
        nome = linhaLimpa[0]

        if len(linhaLimpa) == 4:  # aluno fez AV3
            print(f'Nome: {nome}')  # Resposta questao 1
            gravaNotasAV3(linha)

        if nome not in dados_alunos:
            dados_alunos[nome] = []

        dados_alunos[nome].extend(linhaLimpa[1:])

calcularMediaImprime(dados_alunos)
calcularMinimaMaxima(dados_alunos)
