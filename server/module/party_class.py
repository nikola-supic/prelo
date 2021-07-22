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
        self.anim_head_time = 750
        self.anim_arms = True
        self.anim_arms_time = 750

        self.song_id = None


class Party():
    def __init__(self):
        self.users = {}
        self.queue = {}
        self.likes = set()
        self.dislikes = set()
        self.active_song = {
            'user_id' : None, 
            'queue_id' : None,
            'song_id' : None, 
            'time' : None
        }

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
        char_y = randint(135, 195)

        user = User(user_id, username, (char_x, char_y), char_body, char_head, char_arms)
        self.users[user_id] = user
        print(f'[ + ] Joined. User ID: {user_id}')

    def leave(self, user_id):
        if self.active_song['user_id'] == user_id:
            self.active_song['user_id'] = None

        try:
            self.queue.pop(user_id, None)
        except Exception as e:
            print(str(e))
            print('Error while trying to quit. (queue)')

        try:
            self.users.pop(user_id, None)
        except Exception as e:
            print(str(e))
            print('Error while trying to quit. (users)')
        
        self.users = {}
        self.queue = {}
        self.likes = set()
        self.dislikes = set()
        self.active_song = {
            'user_id' : None, 
            'queue_id' : None,
            'song_id' : None, 
            'time' : None
        }

        print(f'[ + ] Left. User ID: {user_id}')

    def toggle_head(self, user_id, time):
        toggle = self.users[user_id].anim_head
        toggle = False if toggle else True
        self.users[user_id].anim_head = toggle
        self.users[user_id].anim_head_time = time

    def toggle_arms(self, user_id, time):
        toggle = self.users[user_id].anim_arms
        toggle = False if toggle else True
        self.users[user_id].anim_arms = toggle
        self.users[user_id].anim_arms_time = time

    def send_message(self, user_id, username, message):
        self.party_log.info(f'{username}#{user_id:0>4} // {message}')

        with open(self.party_file, 'r') as file:
            return file.read()

    def get_chat(self):
        with open(self.party_file, 'r') as file:
            return file.read()

    def join_queue(self, user_id, song_id):
        self.users[user_id].song_id = song_id
        self.queue[user_id] = self.users[user_id]

    def send_like(self, user_id):
        self.likes.add(user_id)

    def send_dislike(self, user_id):
        self.dislikes.add(user_id)

    def play_song(self, user_id, queue_id, song_id, time):
        print(f'[ + ] Started song: {queue_id}')
        self.active_song = {
            'user_id' : user_id, 
            'queue_id' : queue_id,
            'song_id' : song_id, 
            'time' : time
        }

        del self.queue[queue_id]

    def finish_song(self, user_id):
        song_id = self.active_song['song_id']
        print(f'[ + ] Song finished (ID: {song_id}) // No. likes: {len(self.likes)} // No. dislikes: {len(self.dislikes)}')

        self.likes = set()
        self.dislikes = set()
        self.active_song = {
            'user_id' : None, 
            'queue_id' : None,
            'song_id' : None, 
            'time' : None
        }

    def update_song(self, user_id, ms):
        self.active_song['user_id'] = user_id
        self.active_song['time'] = ms
