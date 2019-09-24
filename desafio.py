#!/usr/bin/python3

import os,shutil
nArquivo = 0
for pasta,subpasta,arquivos in os.walk('/home/v1n1/v1n1/Docs/FIAP'):
    for arquivo in arquivos:
        if arquivo.endswith('.pdf'):
            nArquivo += 1
            shutil.copy(pasta + '/' + arquivo,'/tmp/' + str(nArquivo) + ' ' + arquivo)
