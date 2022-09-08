from core.config import CLIENT

import csv


def index_from_csv(filename):
    dict1 = {}

    csv_filename = filename

    with open(csv_filename) as d:
        reader = csv.DictReader(d)
        for roww in reader:
            id1 = roww["id"]
            title1 = roww["title"]
            dict1[id1] = title1

    with open(csv_filename) as f:
        reader = csv.DictReader(f)
        dict2 = {}
        l = []
        for row in reader:
            parentid = row["parent_id"]
            row.pop("lat_b")
            row.pop("lon_b")
            row.pop("synonyms_b")
            row.pop("address")
            row["state"] = "null"
            if parentid:
                row["parent"] = dict1[parentid]
            else:
                row["parent"] = "null"
            lat1 = row.pop('lat')
            lon1 = row.pop('lon')
            row["_geo"] = {}
            row["_geo"]["lat"] = lat1
            row["_geo"]["lon"] = lon1
            id = row["id"]
            title = row["title"]
            slug = row["slug"]
            parent_id = row["parent_id"]
            parent = row["parent"]
            is_del = row["is_del"]
            state = row["state"]
            _geo = row["_geo"]

            dict2['id'] = id
            dict2['title'] = title
            dict2['slug'] = slug
            dict2['parent_id'] = parent_id
            dict2['parent'] = parent
            dict2['is_del'] = is_del
            dict2['state'] = state
            dict2["_geo"] = {}
            dict2["_geo"]["lat"] = lat1
            dict2["_geo"]["lon"] = lon1
            dict_copy = dict2.copy()

            l.append(dict_copy)
    CLIENT.index('community').add_documents(l)
