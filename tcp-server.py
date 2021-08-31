import socket

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ('', 1337)
skt.bind(server)
skt.listen(10)
while True:
    client, endereco = skt.accept()
    print(f"Cliente {endereco} se conectou!")
    recebido = client.recv(1024).decode()
    print(f"Recibido: {recebido}")
    if recebido == 'Oi servidor\n':
        client.send(b"Oi de volta\n")
    client.close()
