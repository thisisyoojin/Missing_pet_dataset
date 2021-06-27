from math import sin, cos, sqrt, atan2, radians
import pandas as pd


def clean_by_postcode(read_path, save_path):
    df = pd.read_csv(read_path, sep='|')
    cur = df[df['Active postcodes'] > 0]
    cur.drop(columns='Active postcodes', inplace=True)
    cur.to_csv(save_path, index=False)


def get_distance(lat1, long1, lat2, long2):

    # approximate radius of earth in km
    R = 6373.0

    lat1, long1 = radians(lat1), radians(long1)
    lat2, long2 = radians(lat2), radians(long2)

    dlon = long2 - long1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return round(R * c, 3)



def calculate_distance_bewteen_district(read_path, save_path):

    df = pd.read_csv(read_path)
    df = df[['Postcode', 'Latitude', 'Longitude']]
    df.set_index('Postcode', inplace=True)

    for idx in df.index:
        print('starting:',idx)
        test = []
        lat1, long1 = df.loc[[idx]]['Latitude'], df.loc[[idx]]['Longitude']
        for jdx in df.index:
            lat2, long2 = df.loc[[jdx]]['Latitude'], df.loc[[jdx]]['Longitude']
            test.append(get_distance(lat1, long1, lat2, long2))
        df[idx] = test
    df.to_csv(save_path)



if __name__ == "__main__":

    data_path = './barkley/data'
    clean_by_postcode(f'{data_path}/Postcode_districts.csv', f'{data_path}/Available_districts.csv')
    calculate_distance_bewteen_district(f'{data_path}/Available_districts.csv', f'{data_path}/Distance_between_district.csv')

