import codecs
arquivoEscrita = codecs.open('arquivoEscrita.txt', 'w', 'utf-8')

arquivoEscrita.write('Esta é a primeira linha do arquivoEscrita.txt\n', )
arquivoEscrita.write('Esta é a segunda linha do arquivoEscrita.txt\n')

arquivoEscrita.close()

linhas =  ['Esta é a terceira linha do arquivoEscrita.txt\n',
           'Esta é a quarta linha do arquivoEscrita.txt\n']
arquivoLinhas = codecs.open('arquivoLinhas.txt', 'w', 'utf-8')

arquivoLinhas.writelines(linhas)

arquivoLinhas.close()