import os
import json
import numpy as np
# import pandas as pd
from collections import Counter
# import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap

class Location:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

class JSONParser:
    def __init__(self):
        self.wd = os.listdir("../yelp")
        self.businesses = []
        self.location_business_num = Counter()
        self.location_review_num = Counter()
        self.latitudes = []
        self.longitudes = []

    def read_business(self):
        file = open("../yelp/yelp_academic_dataset_business.json", "r")
        lines = file.readlines()
        file.close()
        for b in lines:
            d = json.loads(b)
            if (d["review_count"] > 10):
                self.businesses.append(d)
            # print(d["longitude"], d["latitude"])
        print(self.businesses[0].keys())
        print(lines[0])
        print(len(self.businesses))

    def read_review(self):
        file = open("../yelp/yelp_academic_dataset_review.json", "r")
        # lines = file.readlines()
        # print(lines[0])
        line = file.readline()
        file.close()
        print(line)
        # for b in lines:
        #
        #     d = json.loads(b)
        #     if (d["review_count"] >10):
        #         self.dict.append(d)
        #     # print(d["longitude"], d["latitude"])
        # print(self.dict[0].keys())
        # print(lines[0])
        # print(len(self.dict))

    def read_user(self):
        file = open("../yelp/yelp_academic_dataset_user.json", "r")
        line = file.readline()
        # lines = file.readlines()
        file.close()
        # for b in lines:
            # d = json.loads(b)
            # if (d["review_count"] >10):
            # self.dict.append(d)
            # print(d["longitude"], d["latitude"])
        # print(self.dict[0].keys())
        # print(lines[0])
        # print(len(self.dict))
        print(line)

    def count_reviews(self):
        for business in self.businesses:
            if business['latitude'] is not None and business['longitude'] is not None:
                lat = business['latitude']
                long = business['longitude']

                round_lat = round(lat, 1)
                round_long = round(long, 1)
                # loc = Location(round_lat, round_long)
                current_location = (round_lat, round_long)

                self.location_review_num[current_location] += business['review_count']
                self.location_business_num[current_location] += 1

        for key in self.location_review_num.keys():
            self.latitudes.append(key[0])
            self.longitudes.append(key[1])

        print(len(self.latitudes))
        print(len(self.longitudes))



        # self.less_two_coordinates.append(latitude_list)
        # self.less_two_coordinates.append(longitude_list)

    #parameters: Counter of locations to counts,
    #           list of ordered longitudes and latitudes
    #return: list of ordered
    def create_locations(self, latitudes, longitudes, location_counts):
        review_densities = []

        for index in range(len(latitudes)):
            current_location = (latitudes[index], longitudes[index])
            review_densities.append(location_counts[current_location])

        return review_densities

    def create_review(self, latitudes, longitudes, review_counts):
        review_densities = []

        for index in range(len(latitudes)):
            current_location = (latitudes[index], longitudes[index])
            review_densities.append(review_counts[current_location])

        return review_densities

jp = JSONParser()
# jp.read_business()
# jp.read_business()
jp.read_review()
jp.read_user()
# jp.read_user()
# jp.count_reviews()
# jp.create_map(jp.latitudes, jp.longitudes, jp.location_business_num, jp.location_review_num)
