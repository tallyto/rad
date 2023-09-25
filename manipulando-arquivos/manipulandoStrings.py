with open('arquivo.txt', 'r') as arquivo:
    print("Representação da linha apos strip")
    for linha in arquivo:
        linhaLimpa = linha.strip()
        print(repr(linhaLimpa))
