# Importing the libraries
import socket
from _thread import start_new_thread
from datetime import datetime
import logging
from io import StringIO

# BACKEND CLASS
class Server():
    def __init__(self):
        self.host = 'localhost'
        self.port = 5555
        self.addr = (self.host, self.port)
        self.id_count = 0
        self.addresses = {}
        self.log_file = 'logs/server_log.log'

        logging.basicConfig(filename=self.log_file, filemode='a', format='[ %(asctime)s ] %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
        logging.warning('')
        logging.warning('='*40)
        logging.warning(f'Binding {self.host}:{self.port}')
        
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            self.server.bind((self.host, self.port))
        except socket.error as e:
            print(str(e))


    def start(self):
        logging.warning('Server started, waiting for connection...')
        self.server.listen()
        start_new_thread(self.listening_thread, ())


    def restart(self):
        logging.warning('Restarting server...')


    def shutdown(self):
        logging.warning('Shutting down server...')


    def get_log(self):
        return self.log_file


    def listening_thread(self):
        while True:
            client, client_addr = self.server.accept()
            logging.warning(f'New connection: {client_addr}')

            self.id_count += 1
            self.addresses[client] = client_addr

            start_new_thread(self.client_thread, (client, client_addr))


    def client_thread(self, client, client_addr):
        client.send(str.encode('CONNECTED'))
        while True:
            try:
                data = client.recv(4096).decode()

                if not data:
                    logging.warning(f'Lost connection to: {client_addr}...')
                    break
                else:
                    data_list = data.split()
                    if data_list[0] == 'create':
                        pass

            except Exception as e:
                print(str(e))
                logging.warning(f'Lost connection to: {client_addr}... (Error)')
                break

        self.id_count -= 1
        client.close()
