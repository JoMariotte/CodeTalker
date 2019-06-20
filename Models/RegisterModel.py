from pymongo import MongoClient
import bcrypt


class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codetalker
        self.Users = self.db.users

    def insert_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        userid = self.Users.insert({"username": data.username, "name": data.name, "email": data.email,
                                    "password": hashed, "avatar": "", "background": "", "about": "",
                                    "hobbies": "", "birthday": ""})
