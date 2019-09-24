#!/usr/bin/python3

arq = open("texto.txt", "r")
linha = arq.readlines()

for i in linha: 
         print(i.rstrip())

arq.close()



