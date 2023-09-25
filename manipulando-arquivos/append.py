import codecs

append = codecs.open('arquivoAppend.txt', 'a', 'utf-8')

append.write('Esta é a Última linha do arquivoAppend.txt\n')

append.write('Esta é a Última linha do arquivoAppend.txt\n')

append.close()