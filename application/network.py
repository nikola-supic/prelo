"""
DOCSTRING:

"""
import socket
import pickle

class Network():
    def __init__(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.addr = (self.host, self.port)
        self.first_data = None
        self.connected = False


    def connect(self):
        self.first_data = self.establish_connection()

        if not self.first_data:
            self.connected = False
        else:
            self.connected = True


    def establish_connection(self):
        try:
            print(f'[ > ] Trying connection to: {self.host}:{self.port}')
            self.client.connect(self.addr)
            print(f'[ + ] Successfully connected.')
            return self.client.recv(2048).decode()
        except Exception as e:
            print(e)
            print(f'[ - ] Error while connecting to: {self.host}:{self.port}')
            return False


    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*4))
        except Exception as e:
            print(str(e))


    def download_song(self, data):
        try:
            data_list = data.split()
            song_path = ' '.join(data_list[3:])
            self.client.send(str.encode(data))

            song_size = pickle.loads(self.client.recv(2048*4))

            recived_size = 0
            recived_data = b''
            packet_size = 2048 * 4
            while True:
                packet = self.client.recv(packet_size)
                recived_size += packet_size
                recived_data += packet

                if recived_size > song_size:
                    data_arr = pickle.loads(recived_data) 
                    with open(song_path, 'wb') as file:
                        file.write(data_arr)

                    return song_size


        except Exception as e:
            print(str(e))


    def get_first_data(self):
        return self.first_data