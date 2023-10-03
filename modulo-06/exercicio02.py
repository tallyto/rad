import exercicio01
import os

processarNotas = exercicio01.ProcessadorNotas("onlynotas.txt")

dadosAlunos = processarNotas.ler_arquivo()

arquivo_saida = "onlyNotasAjustado.txt"

try:
    if not dadosAlunos:
        raise ValueError("Não há dados de alunos para processar.")

    with open(arquivo_saida, 'w') as arquivoNotasAjustadas:
        for item in dadosAlunos:
            chave_valor = [f"{key}: {value}" for key, value in item.items()]
            linha = "; ".join(chave_valor)
            arquivoNotasAjustadas.write(linha + "\n")

    if os.path.exists(arquivo_saida):
        print(f"As modificações foram salvas em '{arquivo_saida}'.")
    else:
        print(f"Não foi possível salvar as modificações em '{arquivo_saida}'.")

    with open(arquivo_saida, 'r') as arquivoNotasAjustadas:
        conteudo_modificado = arquivoNotasAjustadas.read()
        print(conteudo_modificado)

except FileNotFoundError:
    print(f"Arquivo de saída '{arquivo_saida}' não encontrado.")
except ValueError as ve:
    print(f"Erro: {ve}")
except Exception as e:
    print(f"Ocorreu um erro não esperado: {e}")
