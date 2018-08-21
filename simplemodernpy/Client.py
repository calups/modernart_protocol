# -*- coding: utf-8 -*-
import socket
import ast

host = '127.0.0.1'
port = 10000
backlog = 10
bufsize = 4096


def connect(agent):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((host, port))

    while(1):
        data = soc.recv(bufsize).decode()
        request=''
        info=''
        arg=''
        try:
            d=ast.literal_eval(data)
            #print(d)
            request=d['request']
            info=d['info']
            if 'arg' in d:
                arg=d['arg']
        except:
            #print(data)
            continue
            #raise Exception("received data can't translate into dict")

        print("Server|", request)      # サーバー側の書き込みを表示
        #print(request)
        #print(info)
        # data = input("Client>")  # 入力待機
        # soc.send(data.encode())              # ソケットに入力したデータを送信
        if request=='INITIALIZE':
            #print('initialize')
            agent.initialize(info)
            soc.send('accept'.encode())

        if request.startswith('PURCHASE'):
            agent.purchase(arg,info)

        if request.startswith('SELL'):
            #print('sell')
            #data = input("Client> ")  # 入力待機
            data=agent.sell(info)
            soc.send(str(data).encode())              # ソケットに入力したデータを送信

        if request.startswith('BID'):
            #print('bid')
            #data = input("Client> ")  # 入力待機
            data=agent.bid(arg,info)
            soc.send(str(data).encode())              # ソケットに入力したデータを送信

        if request.startswith('ROUNDOVER'):
            agent.roundover(arg,info)

        if request.startswith("FINISH"):             # qが押されたら終了
            agent.finish(info)
            soc.close()
            break



if __name__ == '__main__':
    main()
