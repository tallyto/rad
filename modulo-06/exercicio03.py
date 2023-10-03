arquivo_entrada = "onlyNotasAjustado.txt"
arquivo_saida = "onlyNotasAjustadoModificado.txt"

try:
    with open(arquivo_entrada, 'r') as arquivo_entrada:
        linhas = arquivo_entrada.readlines()

    if not linhas:
        raise ValueError("O arquivo de entrada está vazio.")

    with open(arquivo_saida, 'w') as novoArquivo:
        for linha in linhas:
            arrayLinha = linha.strip().split("; ")
            if len(arrayLinha) >= 3:
                chave, valor = arrayLinha[2].split(":")
                if chave == "AV1 ajustada":
                    novo_valor = str(int(valor) + 10)
                    arrayLinha[2] = f"{chave}: {novo_valor}"
                    linha = "; ".join(arrayLinha) + "\n"
            novoArquivo.write(linha)

    print(f"As modificações foram salvas em '{novoArquivo.name}'.")

    # Imprima o arquivo de saída após as modificações


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