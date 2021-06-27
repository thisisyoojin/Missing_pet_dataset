import json


def create_vets_by_postcode():
    vets_by_postcode = {}

    with open('./barkley/data/vets.json', 'r') as f:
        data = json.loads(f.read())



    for d in data:
        district = d['post_code'].split()[0]
        if district in vets_by_postcode.keys():
            vets_by_postcode[district].append(d['id'])
        else:
            vets_by_postcode[district] = [d['id']]


    with open('./barkley/data/vets_by_postcode.json', 'w') as f:
        f.write(json.dumps(vets_by_postcode))


