import socket

HOST = socket.gethostname()
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print('listening')

    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)

            msg = conn.recv(1024)
            print(f'Received {msg}')

            conn.send(bytes("Welcome to the server", "utf-8"))