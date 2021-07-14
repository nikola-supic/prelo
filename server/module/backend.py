# Importing the libraries
import socket
from _thread import start_new_thread
from datetime import datetime

# BACKEND CLASS
class Server():
    def __init__(self):
        self.host = 'localhost'
        self.port = 5555
        self.addr = (self.host, self.port)

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.server.bind((self.host, self.port))
        except socket.error as e:
            print(str(e))

        self.id_count = 0
        self.addresses = {}
        self.log_msgs = []


    def start(self):
        self.add_log('[ + ] Server started, waiting for connection...')
        self.server.listen()
        start_new_thread(self.listening_thread, ())


    def restart(self):
        self.add_log('[ * ] Restarting server...')


    def shutdown(self):
        self.add_log('[ - ] Shutting down server...')

        if len(self.log_msgs):
            time = datetime.now()
            time_str = f'{time.day:02d}_{time.month:02d}_{time.year} {time.hour:02d}_{time.minute:02d}_{time.second:02d}'
            filename = f'logs/log_{time_str}.txt'

            with open(filename, 'w') as file:
                for msg in self.log_msgs:
                    file.write(f'{msg}\n')


    def listening_thread(self):
        while True:
            client, client_addr = self.server.accept()
            self.add_log(f'[ + ] New connection: {client_addr}')

            self.id_count += 1
            self.addresses[client] = client_addr

            start_new_thread(self.client_thread, (client, client_addr))


    def client_thread(self, client, client_addr):
        client.send(str.encode('CONNECTED'))
        while True:
            try:
                data = client.recv(4096).decode()

                if not data:
                    self.add_log(f'[ + ] Lost connection to: {client_addr}...')
                    break
                else:
                    data_list = data.split()
                    if data_list[0] == 'create':
                        pass

            except Exception as e:
                print(str(e))
                self.add_log(f'[ + ] Lost connection to: {client_addr}... (Error)')
                break

        self.id_count -= 1
        client.close()


    def add_log(self, msg):
        time = datetime.now()
        time_str = f'[ {time.hour:02d}:{time.minute:02d}:{time.second:02d} ]'
        msg = f'{time_str} {msg}'
        self.log_msgs.append(msg)
        print(msg)