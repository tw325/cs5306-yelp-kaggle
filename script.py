import os
import json
import numpy as np
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

class Location:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

class JSONParser:
    def __init__(self):
        self.wd = os.listdir("../yelp")
        self.businesses = []
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
        lines = file.readlines()
        file.close()
        for b in lines:
            d = json.loads(b)
            if (d["review_count"] >10):
                self.dict.append(d)
            # print(d["longitude"], d["latitude"])
        print(self.dict[0].keys())
        print(lines[0])
        print(len(self.dict))

    def count_reviews(self):
        for business in self.businesses:
            if business['stars'] < 2.5:
                lat = business['latitude']
                long = business['longitude']

                round_lat = round(lat, 2)
                round_long = round(long, 2)
                # loc = Location(round_lat, round_long)
                current_location = (round_lat, round_long)

                self.latitudes.append(round_lat)
                self.longitudes.append(round_long)
                self.location_review_num[current_location] += 1



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

    def create_map(self, latitudes, longitudes, review_counts):
        review_densities = self.create_locations(latitudes, longitudes, review_counts)
        fig = plt.figure(figsize=(8, 8))
        m = Basemap(projection='lcc', resolution='h',
                    lat_0=37.5, lon_0=-119,
                    width=8E6, height=8E6)
        m.shadedrelief()
        m.drawcoastlines(color='gray')
        m.drawcountries(color='gray')
        m.drawstates(color='gray')

        # 2. scatter city data, with color reflecting population
        # and size reflecting area
        m.scatter(longitudes, latitudes, latlon=True,
                  c=np.log10(review_densities), s=10,
                  cmap='Reds', alpha=0.5)

        # 3. create colorbar and legend
        plt.colorbar(label=r'$\log_{2}({\rm reviewDensities})$')
        plt.clim(3, 7)

        # make legend with dummy points
        for a in [100, 300, 500]:
            plt.scatter([], [], c='k', alpha=0.5, s=10,
                        label=str(10) + ' km$^2$')
        plt.legend(scatterpoints=1, frameon=False,
                   labelspacing=1, loc='lower left');

        plt.show()




jp = JSONParser()
# jp.read_business()
jp.read_business()
# jp.read_user()
jp.count_reviews()
jp.create_map(jp.latitudes, jp.longitudes, jp.location_review_num)
