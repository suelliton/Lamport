# -*- coding: utf-8 -*-

import socket
import time
import threading
import webbrowser
import sys
from random import randint
#cliente
class Cliente(object):

    def __init__(self,i,p,n,f,q,t):
        super(Cliente,self).__init__()
        #global self._tick
        #global self._tick_count
        self._ip = i
        self._port = p
        self._nome = n
        self._faixa = f
        self._qtdProcessos = q
        self._tick = t
        self._tick_count = 0




        threading.Thread(target=self.clock,args=()).start()
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        orig = (self._ip, self._port )
        tcp.bind(orig)
        tcp.listen(1)
        print("Ouvindo em : "+ self._ip)

        while True:

            con, cliente = tcp.accept()
            #print("Cliente "+self._nome+" recebeu no clock :" + str(tick_count))
            self._clkin = self._tick_count
            msg = str(con.recv(1024),"utf-8")
            messages = msg.split("\n")

            nome_origem,clk_origem,tick,ip_origem,ip_destino,mensagem = messages[len(messages)-1].split("-")


            if self._tick_count < int(clk_origem):
                print("modificacao de clock!!")
                print("clock local : "+ str(self._tick_count))
                print("clock recebido : "+ str(clk_origem))
                self._tick_count = int(clk_origem) + 1
                print("correcao de clock : " + str(self._tick_count))

            millis = self._tick_count
            while millis == self._tick_count:#enquanto ainda estiver no clock atual
                pass
            print("tick")

            ip_sort = randint(self._faixa,self._faixa+self._qtdProcessos)#sortea numero final do ip destino
            while "127.0.0."+str(ip_sort) == self._ip:
                ip_sort = randint(self._faixa,self._faixa+self._qtdProcessos)

            ip_destino = "127.0.0."+str(ip_sort)
            dest = (ip_destino, 5000)

            tcpSend = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpSend.connect(dest)

            mensagem = str(int(mensagem)+1)

            msg = msg+"\n"+self._nome+"-"+str(self._tick_count)+"-"+str(self._tick)+"-"+self._ip+"-"+ip_destino+"-"+mensagem
            tcpSend.send(bytes(msg,"utf-8"))

            tcpSend.close()



    def clock(self):
        self._tick_count
        self._tick
        while True:
            #print(str(tick_count))
            #print(".")
            self._tick_count = self._tick_count + self._tick
            time.sleep(self._tick)
