arquivo = open('arquivo.txt', 'r')
print("Arquivo aberto com sucesso!")

conteudo = arquivo.read()
print("Todo conteudo do arquivo",  repr(conteudo), '\n')

conteudoReleitura = arquivo.read()
print("Releitura de todo o conteudo do aquivo")
print(repr(conteudoReleitura), '\n')

arquivo.close()

arquivoReaberto = open('arquivo.txt', 'r')
conteudoReaberto = arquivoReaberto.read()
print("Todo o conteudo do arquivo novamente")
print(repr(conteudoReaberto), '\n')

arquivoReaberto.seek(8)

conteudoSeek = arquivoReaberto.read()
print("Todo conteudo do arquivo apos o SEEK")
print(repr(conteudoSeek))