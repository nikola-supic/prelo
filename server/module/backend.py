# Importing the libraries
import socket
from _thread import start_new_thread
import pickle

from datetime import datetime
import os
from pathlib import Path

# BACKEND CLASS
class Server():
    def __init__(self, root_log, global_log):
        self.host = 'localhost'
        self.port = 5555
        self.addr = (self.host, self.port)
        self.id_count = 0
        self.addresses = {}
        self.root_log = root_log
        self.global_log = global_log

        self.root_log.info('')
        self.root_log.info('='*40)
        self.root_log.info(f'Binding {self.host}:{self.port}')

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            self.server.bind((self.host, self.port))
        except socket.error as e:
            print(str(e))


    def start(self):
        self.root_log.info('Server started, waiting for connection...')
        self.server.listen()
        start_new_thread(self.listening_thread, ())

        self.global_log.info('Started new chat session...')


    def restart(self):
        self.root_log.info('Restarting server...')


    def shutdown(self):
        self.root_log.info('Shutting down server...')


    def listening_thread(self):
        while True:
            client, client_addr = self.server.accept()
            self.root_log.info(f'New connection: {client_addr}')

            self.id_count += 1
            self.addresses[client] = client_addr

            start_new_thread(self.client_thread, (client, client_addr))


    def client_thread(self, client, client_addr):
        client.send(str.encode('CONNECTED'))
        while True:
            try:
                data = client.recv(4096).decode()

                if not data:
                    self.root_log.info(f'Lost connection to: {client_addr}...')
                    break
                else:
                    data_list = data.split()
                    if data_list[0] == 'global':
                        user_id = data_list[1]
                        username = data_list[2]
                        message = data_list[3].replace('_', ' ')

                        chat = self.global_chat(int(user_id), username, message)
                        client.sendall(pickle.dumps(chat))

                    elif data_list[0] == 'get_global':
                        chat = self.get_global_chat()
                        client.sendall(pickle.dumps(chat))

                    elif data_list[0] == 'download':
                        user_id = data_list[1]
                        song_id = data_list[2]
                        song_path = ' '.join(data_list[3:])

                        song_size = os.path.getsize(song_path)
                        client.sendall(pickle.dumps(song_size))

                        with open(song_path, 'rb') as file:
                            client.sendall(pickle.dumps(file.read()))

                        self.root_log.info(f'Downloading song (User ID: {user_id}) (Song ID: {song_id})')


            except Exception as e:
                print(str(e))
                self.root_log.info(f'Lost connection to: {client_addr}... (Error)')
                break

        self.id_count -= 1
        client.close()


    def global_chat(self, user_id, username, message):
        self.global_log.info(f'{username}#{user_id:04} // {message}')

        with open('logs/global_chat.log', 'r') as file:
            return file.read()


    def get_global_chat(self):
        with open('logs/global_chat.log', 'r') as file:
            return file.read()
