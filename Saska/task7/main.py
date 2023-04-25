import osmium as osm


# https://geotree.ru/coordinates?lat=45.06758&lon=38.99979&z=14&mlat=45.060851&mlon=38.972969&c=38.978505,45.035678

# right-top: 45.07352 с.ш. 39.01503 в.д
# left-bottom: 45.04005 с.ш. 38.94636 в.д.

bottom_left = (38.94636, 45.04005)
top_right = (39.01503, 45.07352)


class OsmHandler(osm.SimpleHandler):

    def __init__(self):
        super(OsmHandler, self).__init__()
        self.num_nodes = 0
        self.box = osm.osm.Box(osm.osm.Location(bottom_left[0], bottom_left[1]), osm.osm.Location(top_right[0], top_right[1]))
        self.total_way = 0

    def way(self, w):
        for node in w.nodes:
            if self.box.contains(node.location):
                self.total_way += osm.geom.haversine_distance(w.nodes)


def main():
    h = OsmHandler()
    h.apply_file('map1.osm', locations=True, idx='flex_mem')
    print(h.total_way / 1000)


if __name__ == '__main__':
    main()