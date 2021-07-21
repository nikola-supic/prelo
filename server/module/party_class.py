from random import randint

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


    def join(self, user_id, result):
        username = result[0]

        char_x = randint(0, 370)
        char_y = 150

        char_body = 'images\\art\\torso.png' 
        char_head = 'images\\art\\head.png'
        char_arms = 'images\\art\\arms.png'

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