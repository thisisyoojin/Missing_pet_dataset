from sqlalchemy import create_engine 
import pandas as pd
import db_config

def create_db():
    
    config = db_config.configs
    # setting up the db
    user = config['user'] 
    password = config['password'] 
    host = config['host'] 
    port = config['port'] 
    db_name = config['db_name']
    db_string = f"postgresql://{user}:{password}@{host}:{port}/{db_name}" 

    # create engine
    db = create_engine(db_string) 
    return db


def insert_json_data(json_fpath, table_name, index_col=None):

    db = create_db()

    # open json file
    with open(json_fpath) as f:
        df = pd.read_json(f, orient='records')

    # insert data to db
    if index_col:
        df.set_index(index_col, inplace=True)

    df.to_sql(table_name, db)


def insert_csv_data(csv_fpath, table_name, sep=',', index_col=None):
    
    db = create_db()
    df = pd.read_csv(csv_fpath, sep=sep)
    if index_col:
        df.set_index(index_col, inplace=True)
    df.to_sql(table_name, db)


if __name__ == "__main__":
    insert_json_data('./barkley/data/vets.json', 'vets', index_col='id')
    insert_csv_data('./barkley/data/pet_data/doglost_data.csv', 'doglost', index_col='Dog ID')
    
