import osmium as osm


# https://geotree.ru/coordinates?lat=45.06758&lon=38.99979&z=14&mlat=45.060851&mlon=38.972969&c=38.978505,45.035678

bottom_left = (38.94516, 44.98326)
top_right = (39.05502, 45.11618)


class Handler(osm.SimpleHandler):

    def __init__(self):
        super(Handler, self).__init__()
        self.box = osm.osm.Box(osm.osm.Location(bottom_left[0], bottom_left[1]), osm.osm.Location(top_right[0], top_right[1]))
        self.restaurants = {}
        self.italian_rest = 0
        # self.italian = 0

    def node(self, n):
        name = working_time = 'не известно'
        if 'amenity' in n.tags and n.tags['amenity'] == 'restaurant':
            if 'name' in n.tags:
                name = n.tags['name']
            if 'opening_hours' in n.tags:
                working_time = n.tags['opening_hours']
            # self.restaurants.append((name, work_time))

            if name in self.restaurants.keys():
                self.restaurants[name][0] += 1  # restaurants[name] = (count, working_time)
            else:
                self.restaurants[name] = (1, working_time)

            if 'cuisine' in n.tags and n.tags['cuisine'] == 'italian':
                self.italian_rest += 1
                # self.italian = n.tags['name']


def main():
    h = Handler()
    h.apply_file('map2.osm', locations=True, idx='flex_mem')

    for rest, info in h.restaurants.items():
        print(f'Ресторан: {rest}, Время работы: {info[1]}, Количество: {info[0]}')
    print(f'Из них {h.italian_rest} с итальянской кухней')
    # print(h.italian)


if __name__ == '__main__':
    main()