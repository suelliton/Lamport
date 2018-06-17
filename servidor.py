import socket
import time
import threading
from random import randint
#cliente
tick = 0
tick_count = 0
class Servidor(object):

    def __init__(self,ip,port,t, n,f,qtd):
        super(Servidor,self).__init__()

        self._ip = ip
        self._port = port
        self._nome = n
        self._faixa = f
        self._qtdProcessos = qtd
        self._tick = t
        self._tick_count = 0

        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        threading.Thread(target=self.clock,args=()).start()


        ip_sort = randint(self._faixa+1,self._faixa+self._qtdProcessos)#sortea numero final do ip destino
        while "127.0.0."+str(ip_sort) == self._ip:
            ip_sort = randint(self._faixa+1,self._faixa+self._qtdProcessos)
        print("bufo")

        ip_destino = "127.0.0."+str(ip_sort)
        dest = (ip_destino, 5000)
        tcp.connect(dest)

        millis = self._tick_count
        while millis > millis + (self._tick * 2):#enquanto ainda estiver no clock atual
            print("huhudidir hihihi")


        msg = self._nome+"-"+str(self._tick_count)+"-"+str(self._tick)+"-"+str(self._ip)+"-"+ip_destino+"-"+str(1)
        tcp.send(bytes(msg,"utf-8"))
        print(msg)
        print("Servidor enviou no clock : "+ str(self._tick_count))
        self.exibeMensagem(self._nome, str(self._tick_count),str(self._tick),self._ip,ip_destino,str(1))


        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        orig = (self._ip, self._port )
        tcp.bind(orig)
        tcp.listen(1)
        while True:

            con, cliente = tcp.accept()
            self._clkin = self._tick_count
            #print("Servidor recebeu no clock :" + str(tick_count))

            msg = str(con.recv(1024),"utf-8")

            print(msg)
            messages = msg.split("\n")
            for m in messages:
                nome_origem,clk_origem,tick,ip_origem, ip_destino,mensagem = m.split("-")
                self.exibeMensagem(nome_origem,clk_origem,tick,ip_origem,ip_destino,mensagem)
            print("\n")
            if self._tick_count < int(clk_origem):
                self._tick_count = int(clk_origem) + 1
                print("correcao de clock :" + str(self._tick_count))

            self.exibeMensagem(self._nome ,str(self._tick_count),tick,self._ip,self._ip,"")

            print("\n\n------------------------CAMINHO PERCORRIDO----------------------------------")
            for m in messages:
                nome_origem,clk_origem,tick,ip_origem,ip_destino,mensagem = m.split("-")
                print(nome_origem+ " | ",end='',flush=True)
            print("servidor |")
            print("\n--------------------------------------------------------")
            if(ip_destino == self._ip):
                print("terminou!!!")
                break




        tcp.close()

    def clock(self):
        while True:
            #print(str(tick_count))
            self._tick_count = self._tick_count + self._tick
            time.sleep(self._tick)

    def exibeMensagem(self,nome,clk_origem,tick,origem,destino,mensagem):
        print("------------------------------------------------------------------")
        if len(nome) > 4:
            print("|   nome    |clk_origem| tick  |   origem   |    destino   |  msg  |")
            print("|  "+nome+" |     "+clk_origem+       "    |   "+tick+"   |"+origem+" | "+destino+"  |  "+mensagem+"   |")
        else:
            print("|   nome    |clk_origem|   tick    |  origem  |    destino   |  msg  |")
            print("|    "+nome+"     |    "+clk_origem+"    | "+origem+"  |  "+destino+"  |   "+mensagem+" | ")
        print("------------------------------------------------------------------")
