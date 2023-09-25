print("Interando sobre o arquivo")

with open('arquivo.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)
    print("Fim do arquivo", arquivo.name)