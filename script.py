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
        self.location_stars = Counter()

    def read_business(self):
        file = open("../yelp/yelp_academic_dataset_business.json", "r")
        lines = file.readlines()
        file.close()
        for b in lines:
            d = json.loads(b)
            # if (d["review_count"] > 10):
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
            if business['stars'] <= 2.5 and business['latitude'] is not None and business['longitude'] is not None:
                lat = business['latitude']
                long = business['longitude']

                round_lat = round(lat, 2)
                round_long = round(long, 2)
                # loc = Location(round_lat, round_long)
                current_location = (round_lat, round_long)

                self.location_review_num[current_location] += business['review_count']
                self.location_business_num[current_location] += 1
                self.location_stars[current_location] += business['stars']

        for key in self.location_review_num.keys():
            self.latitudes.append(key[0])
            self.longitudes.append(key[1])

        print(len(self.latitudes))
        print(len(self.longitudes))

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

    def create_stars(self, latitudes, longitudes, stars, business_count):
        star_densities = []

        for index in range(len(latitudes)):
            current_location = (latitudes[index], longitudes[index])
            star_densities.append(stars[current_location]/business_count[current_location])

        return star_densities

    def create_map(self, latitudes, longitudes, business_counts, review_counts, stars):
        location_densities = self.create_locations(latitudes, longitudes, business_counts)
        review_densities = self.create_review(latitudes, longitudes, review_counts)
        star_densities = self.create_stars(latitudes, longitudes, stars, business_counts)

        #Las Vegas, Nevada
        fig = plt.figure(figsize=(8, 8))

        m = Basemap(llcrnrlon=-116,llcrnrlat=35,urcrnrlon=-114,urcrnrlat=37,
        projection='lcc',lat_1=33,lat_2=45,lon_0=-95, resolution='h')
        m.drawcoastlines(color='gray')
        m.drawcountries(color='gray')
        m.drawstates(color='black')

        # plt.clim(1,5)
        # plt.colorbar(label='Review Densities')


        # 2. scatter city data, with color reflecting population
        # and size reflecting area
        m.scatter(longitudes, latitudes, latlon=True,
                  c=star_densities, s=1,
                  cmap='RdYlGn', alpha=1)


        #Madison, Wisconson

        # fig2 = plt.figure(figsize=(8, 8))
        #
        #
        #
        # m2 = Basemap(llcrnrlon=-90,llcrnrlat=42,urcrnrlon=-88,urcrnrlat=44,
        # projection='lcc',lat_1=33,lat_2=45,lon_0=-95, resolution='h')
        # m2.drawcoastlines(color='gray')
        # m2.drawcountries(color='gray')
        # m2.drawstates(color='black')
        #
        # # 2. scatter city data, with color reflecting population
        # # and size reflecting area
        # m2.scatter(longitudes, latitudes, latlon=True,
        #           c=star_densities, s=1,
        #           cmap='RdYlGn', alpha=1)

        #Cleveland, Ohio
        fig2 = plt.figure(figsize=(8, 8))

        m2 = Basemap(llcrnrlon=-83,llcrnrlat=40.5,urcrnrlon=-81,urcrnrlat=42.5,
        projection='lcc',lat_1=33,lat_2=45,lon_0=-95, resolution='h')
        m2.drawcoastlines(color='gray')
        m2.drawcountries(color='gray')
        m2.drawstates(color='black')

        # 2. scatter city data, with color reflecting population
        # and size reflecting area
        m2.scatter(longitudes, latitudes, latlon=True,
                  c=star_densities, s=1,
                  cmap='RdYlGn', alpha=1)

        # fig3 = plt.figure(figsize=(8, 8))
        # m3 = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        # projection='lcc',lat_1=33,lat_2=45,lon_0=-95, resolution='h')
        # m3.drawcoastlines(color='gray')
        # m3.drawcountries(color='gray')
        # m3.drawstates(color='black')
        #
        # # 2. scatter city data, with color reflecting population
        # # and size reflecting area
        # m3.scatter(longitudes, latitudes, latlon=True,
        #           c=np.log10(review_densities), s=1,
        #           cmap='Oranges', alpha=1)

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

# jp.count_reviews()
# jp.create_map(jp.latitudes, jp.longitudes, jp.location_business_num, jp.location_review_num)
jp.count_reviews()
jp.create_map(jp.latitudes, jp.longitudes, jp.location_business_num, jp.location_review_num, jp.location_stars)
