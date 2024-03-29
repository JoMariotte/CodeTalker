from pymongo import MongoClient
import bcrypt


class LoginModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codetalker
        self.Users = self.db.users

    def check_user(self, data):
        user = self.Users.find_one({"username": data.username})
        if user:
            if bcrypt.checkpw(data.password.encode(), user["password"]):
                return user
            else:
                return False
        else:
            return False
