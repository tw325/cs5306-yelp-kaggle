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
        lines = file.readlines()
        file.close()
        for b in lines:
            d = json.loads(b)
            # if (d["review_count"] >10):
            self.dict.append(d)
            # print(d["longitude"], d["latitude"])
        print(self.dict[0].keys())
        print(lines[0])
        print(len(self.dict))

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

    def create_map(self, latitudes, longitudes, business_counts, review_counts):
        location_densities = self.create_locations(latitudes, longitudes, business_counts)
        review_densities = self.create_review(latitudes, longitudes, review_counts)
        fig = plt.figure(figsize=(10, 10))
        m = Basemap(llcrnrlon=-116,llcrnrlat=35,urcrnrlon=-113,urcrnrlat=38,
        projection='lcc',lat_1=33,lat_2=45,lon_0=-95, resolution='h')
        m.shadedrelief()
        m.drawcoastlines(color='gray')
        m.drawcountries(color='gray')
        m.drawstates(color='gray')

        # 2. scatter city data, with color reflecting population
        # and size reflecting area
        m.scatter(longitudes, latitudes, latlon=True,
                  c=review_densities, s=location_densities,
                  cmap='cool', alpha=0.2)

        # 3. create colorbar and legend
        # plt.colorbar(label=r'$\log_{2}({\rm reviewDensities})$')
        # plt.clim(3, 7)
        #
        # # make legend with dummy points
        # for a in [100, 300, 500]:
        #     plt.scatter([], [], c='k', alpha=0.5, s=10,
        #                 label=str(10) + ' km$^2$')
        # plt.legend(scatterpoints=1, frameon=False,
        #            labelspacing=1, loc='lower left');

        plt.show()




jp = JSONParser()
# jp.read_business()
jp.read_business()
# jp.read_user()
jp.count_reviews()
jp.create_map(jp.latitudes, jp.longitudes, jp.location_business_num, jp.location_review_num)
