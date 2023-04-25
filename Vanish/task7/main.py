import osmium as osm


# https://geotree.ru/coordinates?lat=45.06758&lon=38.99979&z=14&mlat=45.060851&mlon=38.972969&c=38.978505,45.035678

# right-top: 45.07352 с.ш. 39.01503 в.д
# left-bottom: 45.04005 с.ш. 38.94636 в.д.

bottom_left = (38.94636, 45.04005)
top_right = (39.01503, 45.07352)


class Handler(osm.SimpleHandler):

    def __init__(self):
        super(Handler, self).__init__()
        self.box = osm.osm.Box(osm.osm.Location(bottom_left[0], bottom_left[1]), osm.osm.Location(top_right[0], top_right[1]))
        self.all_day_work = 0
        self.supermarkets = {}
        # self.total_way = 0

    def node(self, n):
        if 'name' in n.tags and 'shop' in n.tags and n.tags['shop'] == 'supermarket':
            if 'opening_hours' in n.tags and n.tags['opening_hours'] == '24/7':
                self.all_day_work += 1
            if self.supermarkets.setdefault(n.tags['name']) is not None:
                self.supermarkets[n.tags['name']] += 1
            else:
                self.supermarkets[n.tags['name']] = 1


    # def way(self, w):
    #     for node in w.nodes:
    #         if self.box.contains(node.location):
    #             self.total_way += osm.geom.haversine_distance(w.nodes)


def main():
    h = Handler()
    h.apply_file('map1.osm', locations=True, idx='flex_mem')
    # print(h.total_way / 1000)
    for shop, count in h.supermarkets.items():
        print(shop, count)

    print(f'Количество круглосуточных: {h.all_day_work}')


if __name__ == '__main__':
    main()