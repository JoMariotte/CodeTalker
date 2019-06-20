from pymongo import MongoClient


class Posts:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codetalker
        self.Users = self.db.users
        self.Posts = self.db.posts

    def insert_posts(self, data):
        inserted = self.Posts.insert({"username": data.username, "content": data.content})
        return True

    def get_all_posts(self):
        all_posts = self.Posts.find()
        posts_for_front = []
        for post in all_posts:
            post["user"] = self.Users.find_one({"username": post["username"]})
            posts_for_front.append(post)
        return posts_for_front
