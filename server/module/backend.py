# Importing the libraries
import socket
from _thread import start_new_thread
import pickle

import os
from module.party_class import Party
import db_server as db

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

        self.party = Party()


    def start(self):
        self.root_log.info('Server started, waiting for connection...')
        self.server.listen()
        start_new_thread(self.listening_thread, ())

        self.global_log.info('Started new chat session...')


    def restart(self):
        del self.party
        self.party = Party()

        self.root_log.info('Restarting server...')


    def shutdown(self):
        del self.party
        self.party = Party()

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

                    elif data_list[0] == 'join_party':
                        user_id = data_list[1]

                        result = db.get_party_user(user_id)
                        self.party.join(user_id, result)
                        client.sendall(pickle.dumps(self.party))

                    elif data_list[0] == 'leave_party':
                        user_id = data_list[1]

                        self.party.leave(user_id)
                        client.sendall(pickle.dumps(self.party))

                    elif data_list[0] == 'get_party':
                        client.sendall(pickle.dumps(self.party))

                    elif data_list[0] == 'toggle_head':
                        user_id = data_list[1]

                        self.party.toggle_head(user_id)
                        client.sendall(pickle.dumps(self.party))

                    elif data_list[0] == 'toggle_arms':
                        user_id = data_list[1]

                        self.party.toggle_arms(user_id)
                        client.sendall(pickle.dumps(self.party))

                    elif data_list[0] == 'send_message':
                        user_id = data_list[1]
                        username = data_list[2]
                        username.replace('_', ' ')
                        message = ' '.join(data_list[3:])

                        chat = self.party.send_message(user_id, username, message)
                        client.sendall(pickle.dumps(chat))

                    elif data_list[0] == 'get_chat':
                        chat = self.party.get_chat()
                        client.sendall(pickle.dumps(chat))

                    elif data_list[0] == 'join_queue':
                        user_id = data_list[1]
                        song_id = data_list[2]

                        self.party.join_queue(user_id, song_id)
                        client.sendall(pickle.dumps(self.party.queue))

                    elif data_list[0] == 'send_like':
                        user_id = data_list[1]

                        self.party.send_like(user_id)
                        client.sendall(pickle.dumps(self.party.likes))

                    elif data_list[0] == 'send_dislike':
                        user_id = data_list[1]

                        self.party.send_dislike(user_id)
                        client.sendall(pickle.dumps(self.party.dislikes))

            except Exception as e:
                print(str(e))
                self.root_log.info(f'Lost connection to: {client_addr}... (Error)')
                break

        self.addresses.pop(client)
        self.id_count -= 1
        client.close()

    def global_chat(self, user_id, username, message):
        self.global_log.info(f'{username}#{user_id:0>4} // {message}')

        with open('logs/global_chat.log', 'r') as file:
            return file.read()

    def get_global_chat(self):
        with open('logs/global_chat.log', 'r') as file:
            return file.read()
