from random import randint
import logging

class User():
    def __init__(self, user_id, username, pos, body, head, arms):
        self.user_id = user_id
        self.username = username
        self.pos = pos
        self.x, self.y = pos
        self.size = (100, 220)
        self.width, self.height = (100, 220)
        self.body = body
        self.head = head
        self.arms = arms

        self.anim_head = True
        self.anim_arms = True


class Party():
    def __init__(self):
        self.users = {}

        self.party_file = 'logs/party_chat.log'
        self.party_log = logging.getLogger('PARTY')
        self.party_log.setLevel(logging.INFO)
        handler = logging.FileHandler(self.party_file, 'w', 'utf-8')
        formatter = logging.Formatter('[ %(asctime)s ] %(message)s', datefmt='%H:%M:%S')
        handler.setFormatter(formatter)
        self.party_log.addHandler(handler)

    def join(self, user_id, result):
        username = result[0]

        char_body = 'images\\art\\torso.png' 
        char_head = 'images\\art\\head.png'
        char_arms = 'images\\art\\arms.png'

        char_x = randint(0, 370)
        char_y = randint(150, 195)

        user = User(user_id, username, (char_x, char_y), char_body, char_head, char_arms)
        self.users[user_id] = user

    def leave(self, user_id):
        self.users.pop(user_id)

    def toggle_head(self, user_id):
        toggle = self.users[user_id].anim_head
        toggle = False if toggle else True
        self.users[user_id].anim_head = toggle

    def toggle_arms(self, user_id):
        toggle = self.users[user_id].anim_arms
        toggle = False if toggle else True
        self.users[user_id].anim_arms = toggle

    def send_message(self, user_id, username, message):
        self.party_log.info(f'{username}#{user_id:0>4} // {message}')

        with open(self.party_file, 'r') as file:
            return file.read()

    def get_chat(self):
        with open(self.party_file, 'r') as file:
            return file.read()