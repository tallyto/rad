class ProcessadorNotas:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.dados_alunos = []

    def calcular_av1_ajustada(self, av1):
        return av1 + 10

    def ler_arquivo(self):
        try:
            with open(self.nome_arquivo, "r") as arquivo:
                linhas = arquivo.readlines()

            if not linhas:
                raise ValueError("O arquivo está vazio.")

            for linha in linhas:
                conteudo = linha.strip().split(";")
                if len(conteudo) >= 2:
                    matricula = conteudo[0]
                    av1 = int(conteudo[1])
                    av1_ajustada = self.calcular_av1_ajustada(av1)

                    self.dados_alunos.append({
                        "Matricula": matricula,
                        "AV1": av1,
                        "AV1 ajustada": av1_ajustada
                    })

            if not self.dados_alunos:
                raise ValueError("Nenhum dado de aluno válido encontrado no arquivo.")

            return self.dados_alunos

        except FileNotFoundError:
            print(f"Arquivo não encontrado: {self.nome_arquivo}. Verifique o nome do arquivo ou o caminho.")
        except ValueError as ve:
            print(f"Erro: {ve}")
        except Exception as e:
            print(f"Ocorreu um erro não esperado: {e}")

    def mostrar_dados_alunos(self):
        for aluno in self.dados_alunos:
            print("--------------------------")
            print(f"Matricula: {aluno['Matricula']}\n"
                  f"AV1: {aluno['AV1']}\n"
                  f"AV1 ajustada: {aluno['AV1 ajustada']}")
            print("--------------------------")


if __name__ == "__main__":
    processador = ProcessadorNotas("onlynotas.txt")
    dados_alunos = processador.ler_arquivo()
    if dados_alunos:
        processador.mostrar_dados_alunos()
