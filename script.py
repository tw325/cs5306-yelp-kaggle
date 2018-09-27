import os
import json

class JSONParser:
    def __init__(self):
        self.wd = os.listdir("../yelp")
        self.dict = []

    def read(self):
        file = open("../yelp/yelp_academic_dataset_business.json", "r")
        lines = file.readlines()
        file.close()
        for b in lines:
            d = json.loads(b)
            if (d["review_count"] >10):
                self.dict.append(d)
            # print(d["longitude"], d["latitude"])
        print(self.dict[0].keys())
        # print(self.dict[)
        print(lines[0])
        print(len(self.dict))

jp = JSONParser()
jp.read()
