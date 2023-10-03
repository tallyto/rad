arquivo_entrada = "onlynotas.txt"
arquivo_saida = "onlyNotasAv1Av2.txt"

try:
    with open(arquivo_entrada, 'r') as arquivo_entrada:
        linhas = arquivo_entrada.readlines()

    if not linhas:
        raise ValueError("O arquivo de entrada está vazio.")

    with open(arquivo_saida, 'w') as novoArquivo:
        for linha in linhas:
            conteudo = linha.strip().split(";")
            matricula = conteudo[0]
            av1 = int(conteudo[1])
            av2 = int(conteudo[2])

            if len(conteudo) >= 4:
                av3 = int(conteudo[3])
            else:
                av3 = None

            if av3 is not None:
                novo_av1 = av1 + 2
                novo_av2 = av2 + 3
                novo_av3 = av3 + 4
                linha = f"{matricula};{novo_av1};{novo_av2};{novo_av3}\n"
            else:
                novo_av1 = av1 + 2
                novo_av2 = av2 + 3
                linha = f"{matricula};{novo_av1};{novo_av2}\n"

            novoArquivo.write(linha)

    print(f"As modificações foram salvas em '{novoArquivo.name}'.")

except FileNotFoundError:
    print(f"Arquivo de entrada '{arquivo_entrada}' não encontrado.")
except ValueError as ve:
    print(f"Erro: {ve}")
except Exception as e:
    print(f"Ocorreu um erro não esperado: {e}")
finally:
    with open(arquivo_saida, 'r') as arquivo_saida_leitura:
        conteudo_modificado = arquivo_saida_leitura.read()
        print(conteudo_modificado)
