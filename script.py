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

def drawMap(long, lat, review_count):
    # 1. Draw the map background
    fig = plt.figure(figsize=(8, 8))
    m = Basemap(projection='lcc', resolution='h',
                lat_0=long, lon_0=-lat,
                width=1E6, height=1.2E6)
    m.shadedrelief()
    m.drawcoastlines(color='gray')
    m.drawcountries(color='gray')
    m.drawstates(color='gray')

    # 2. scatter city data, with color reflecting population
    # and size reflecting area
    m.scatter(lon, lat, latlon=True,
              c=np.log10(review_count), s=area,
              cmap='Reds', alpha=0.5)

    # 3. create colorbar and legend
    plt.colorbar(label=r'$\log_{10}({\rm review_count})$')
    plt.clim(3, 7)

    # make legend with dummy points
    for a in [100, 300, 500]:
        plt.scatter([], [], c='k', alpha=0.5, s=a,
                    label=str(a) + ' km$^2$')
    plt.legend(scatterpoints=1, frameon=False,
               labelspacing=1, loc='lower left');
