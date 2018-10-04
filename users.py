import os
import json


class Users:
    def __init__(self):
        self.users = []
        self.dict = {}

    def read_user(self):
        file = open("../yelp/yelp_academic_dataset_user.json", "rb")
        lines = file.readlines()
        file.close()
        print(len(lines))
        # for b in lines:
        #     d = json.loads(b)
        #     if (d["review_count"] > 10):
        #         self.businesses.append(d)


users = Users()
users.read_user()
