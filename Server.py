from __future__ import print_function
import socket
import select

host = '127.0.0.1'
port = 10000
backlog = 10
bufsize = 4096

playersize = 3


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))    # 指定したホスト(IP)とポートをソケットに設定
    s.listen(3)                     # 1つの接続要求を待つ
    soc, addr = s.accept()          # 要求が来るまでブロック
    print("Conneted by"+str(addr))  # サーバ側の合図

    while (1):
        data = input("Server>")  # 入力待機(サーバー側)
        soc.send(data.encode())              # ソケットにデータを送信
        data = soc.recv(bufsize).decode()       # データを受信（1024バイトまで）
        print("Client>", data)       # サーバー側の書き込みを表示
        if data == "q":             # qが押されたら終了
            soc.close()
            break


def connect(size):
    socks = []
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(size)
    print('waiting for',size, 'connection...')
    for i in range(size):
        soc, addr = s.accept()          # 要求が来るまでブロック
        socks.append(soc)
        print(len(socks), "Conneted by", str(addr),)  # サーバ側の合図
    print('successfully connected with', len(socks), 'clients.')

    for soc in socks:
        soc.send('INITIALIZE'.encode())

    tmp = 0
    for soc in socks:
        tmp += 1
        data = soc.recv(bufsize).decode()
        print('Client[' + str(tmp) + ']> ', data)
        if data != 'accept':
            raise Exception('initialize failed.')
    return socks

def request_sell(sock):
    msg='SELL'
    print(msg)
    sock.send(bytes(msg, 'utf-8'))
    recv = sock.recv(bufsize).decode()
    result=-1
    try:
        result=int(recv)
    except:
        raise Exception('painting id must be int.')
    return int(recv)

def request_bid(sock):
    msg = 'BID'
    print(msg)
    sock.send(bytes(msg, 'utf-8'))
    recv = sock.recv(bufsize).decode()
    return int(recv)


if __name__ == '__main__':
    connect(3)
