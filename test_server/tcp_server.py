from socket import *
HOST = ''
PORT = 9999
BUFSIZ = 256
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)   #创建套接字
tcpSerSock.bind(ADDR)   #绑定IP和端口
tcpSerSock.listen(5)    #监听端口，最多5人排队

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()    #建立连接
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        data =data.decode('utf-8')
        print(data)
        split_data = data.split(",")
        file = open(file=split_data[0]+".csv",mode='a')
        file.write(data)
        file.close()
    tcpCliSock.close()
tcpSerSock.close()