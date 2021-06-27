#%%
import pandas as pd
import json


def convert_to_json(txt_path, json_path):

    with open(txt_path, 'r') as f:
        data = f.readlines()

    with open(json_path, 'w') as f:
        f.write(json.dumps([json.loads(d.strip('\n')) for d in data]))


def get_df_from_json(json_path):
    with open(json_path, 'r') as f:
        df = pd.read_json(f, orient='records')
    return df


def clean_data(df):    
    df.dropna(subset=['Status'], inplace=True)



def get_postarea(df):

    def extract_postcode(row):

        if row['Lost In Post Area'] == row['Found In Post Area'] or type(row['Found In Post Area']) == float:
            return row['Lost In Post Area']
        
        elif type(row['Lost In Post Area']) == float:
            return row['Found In Post Area']

        else:
            if row['Status'] == 'Reunited':
                return row['Found In Post Area']
            else:
                return row['Lost In Post Area']

    df['Post Area'] = df.apply(lambda r: extract_postcode(r), axis=1)



def preprocess_data(txt_path, json_path):
    convert_to_json(txt_path, json_path)
    df = get_df_from_json(json_path)
    clean_data(df)
    get_postarea(df)
    return df


def add_district_info(df):
    av = pd.read_csv('./barkley/data/Available_districts.csv')
    district_info = av[['Postcode', 'Town/Area', 'Population', 'Households']]
    df = df.merge(district_info, how='left', left_on='Post Area', right_on='Postcode')
    return df



def add_nearby_vets(df):
    
    dist = pd.read_csv('./barkley/data/Distance_between_district.csv')

    with open('./barkley/data/vets_by_postcode.json') as f:
        vets_by_postcode = json.loads(f.read())


    def impute_vets(district, radius):
        if district in vets_by_postcode.keys():
            vets = []
            nearby_vets = dist[dist[district] <= radius]['Area']
            for nearby in nearby_vets:
                if nearby in vets_by_postcode.keys():
                    vets.extend(vets_by_postcode[nearby])
            return vets
        else:
            return []

    df['Post Area_Vets in 5'] = df['Post Area'].apply(lambda x: impute_vets(x,5))
    df['Post Area_Vets in 10'] = df['Post Area'].apply(lambda x: impute_vets(x,10))
    

def save_data(df):
    df.to_csv('./barkley/data/pet_data/doglost_data.csv', index=False)



if __name__ == "__main__":

    params = {
        "txt_path": "./barkley/data/pet_data/doglost_data.txt",
        "json_path": "./barkley/data/pet_data/doglost_data.json"
    }

    df = preprocess_data(**params)
    df = add_district_info(df)
    add_nearby_vets(df)
    save_data(df)

