from servidor import Servidor
from cliente import Cliente
from random import randint
import threading
import os
import time
import sys




def makeProcess(ip,port,tick,nome,faixa,qtdProcessos):
    Cliente(ip,port,nome,faixa,qtdProcessos,tick)
    exibeProcesso(nome,ip,tick)


def main():
    if sys.argv[1]:
        faixa = int(sys.argv[1])
    else:
        faixa = 102
    if sys.argv[2]:
        qtdProcessos = int(sys.argv[2])
    else:
        qtdProcessos = 4

    hosts = range(faixa+1,faixa+qtdProcessos+1)

    for host in hosts:
        print("hosts "+str(host))

    cont = 1
    for host in hosts:
        sort = randint(2,10)
        print("sorteadooo  " +str(sort))
        threading.Thread(target=makeProcess,args=("127.0.0."+str(host),5000,sort,"p"+str(cont),faixa,qtdProcessos)).start()
        cont =cont+1




    Servidor("127.0.0."+str(faixa),5000,randint(2,10),"servidor",faixa,qtdProcessos)


def exibeProcesso(nome,ip,tick):
    print("---------------------------------------------------------")
    print("|    nome    |      ip     |    tick     |")
    print("|  "+nome+"  |  "+ip+"  |  "+tick+"   |")
    print("---------------------------------------------------------")






if __name__ == '__main__':
    main()
